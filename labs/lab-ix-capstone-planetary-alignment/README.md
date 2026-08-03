# Lab IX: Capstone Project — Predicting a Planetary Alignment

**Programming Essentials for Astronomy I — Python**

Everything you have built this semester comes together here. You will make your
own measurements of where Venus, Earth and Mars sit in their orbits, write code
that turns those measurements into a **physical model** of the Solar System, and
use that model to **predict a date in the future** — the next time the three
planets line up.

Then you will check whether you were right.

This is what computational astrophysics actually looks like: measure something,
fit a model, extrapolate, and then be honest about how wrong you were and why.
Unlike every previous lab, **nobody is going to tell you the answer** — your code
either predicts the right date or it doesn't.

---

## Learning goals

By the end of this project you should be able to:

1. Turn a **physical question** into a sequence of code you can actually write.
2. Read a real measurement table into **NumPy** and fit a model to it.
3. Understand why **how you sample** your data limits what you can conclude.
4. Find where a function **crosses zero**, and know why that is easier and safer
   than looking for where it is smallest.
5. Show a result honestly with a **Matplotlib** figure that makes its own point.
6. Judge your own answer: quote an uncertainty, and defend it.

---

## The project in two parts

| | Where | What you do | Time |
|---|---|---|---|
| **Part 1** | The Digital Dome | Fly to a viewpoint above the Solar System and measure the positions of Venus, Earth and Mars at 12 moments spread over roughly two years of simulated time. | One session |
| **Part 2** | The Computer Lab | Derive and code `next_alignment(...)`: a function that takes those measurements and returns the date of the next alignment. Then verify it. | Two sessions |

You finish with a short **report** and a **presentation** to the class (Part 3
below).

### What counts as an "alignment"

This turns out to be the most important decision in the whole project, so we make
it for you — and in your report you will explain why it matters.

"The planets are aligned" is a vague phrase. Demanding that Venus, Earth and Mars
all sit at the **same direction from the Sun** is so restrictive that it happens
roughly twice a century, and predicting an event that far ahead from two years of
data is hopeless. Worse, it forces you to invent a tolerance — "within 15°, say" —
and your answer then depends on that arbitrary choice.

So instead, our alignment is:

> **Earth, Venus and Mars lying on a straight line, with Earth at one end.**

This is exactly the moment when, standing on Earth, you see **Venus and Mars in
the same place in the sky**. It is a real three-planet alignment, it happens
often enough to predict from your data, it needs no arbitrary tolerance — and
best of all, you can *look* at it in the dome and see whether you were right.

---

# Part 1 — The Dome Visit

## The problem with the obvious approach

If you stand outside and watch Mars, you are watching from a moving platform.
Mars appears to slow down, stop, and go *backwards* for a few weeks each year
(**retrograde motion**) — not because Mars reverses, but because Earth overtakes
it. Positions measured from Earth are the *sum* of two motions tangled together.

To model orbits, we want to untangle them. So we cheat, in a way only a digital
dome lets us: **we move the observer to the Sun.** From there, each planet simply
marches steadily around its orbit, and the numbers become something you can fit a
straight line to.

## What you are measuring

For each planet, at each moment in time, you record its **heliocentric ecliptic
longitude** — call it λ. This is one number, in degrees from 0 to 360: the
direction from the Sun to the planet, measured in the plane of Earth's orbit.
Think of the Solar System as a clock face seen from above; λ is where the planet's
hand is pointing.

Optionally (see Part 2) you also record the planet's **distance from the Sun** in
AU. Your code can work without it, but recording it opens up the better of the
two models.

## The measurement protocol

Your demonstrator will set the dome to a viewpoint centred on the Sun and turn on
the readout showing ecliptic longitude and distance.

1. Note the **starting date** the dome is set to. Write it down. Everything else
   is measured in days after this.
2. Record λ for **Venus, Earth and Mars**.
3. Step the simulation forward **60 days**.
4. Repeat until you have **12 sets of measurements** — about 690 days, or roughly
   one full orbit of Mars.

Record everything in a plain CSV file, `measurements.csv`, in this format:

```
# days_since_start, lon_venus, lon_earth, lon_mars, r_venus, r_earth, r_mars
0,   253.72, 306.51,  52.17, 0.7259, 1.0153, 1.4770
60,  348.72,   4.52,  83.81, 0.7272, 1.0022, 1.5544
...
```

(Those two rows are the real values for a start date of 30 July 2026. Your dome
session may start on a different date — use what you measure, not what is printed
here. Notice already that Venus has moved 95°, Earth 58° and Mars only 32°: the
inner planets really do run faster.)

> **Working as a class.** Reading 12 × 6 numbers off a dome screen is slow. Your
> demonstrator may split the class into groups, with each group responsible for a
> few epochs, and pool the results into one shared CSV. If so, be aware that
> pooled data always contains at least one typo. Finding it is part of the job —
> a longitude that breaks the smooth trend is a transcription error, not a
> discovery.

## Two things to understand before you leave the dome

### Why 60 days, and why 690?

Both numbers are deliberate, and getting either wrong quietly ruins the result.

**The span (690 days) is set by Mars.** Mars's orbit is noticeably
non-circular, so it does not move at a constant rate — it runs fast when close to
the Sun and slow when far away. Measure it over a short arc and you measure
whichever speed it happens to have *right now*, then wrongly assume that speed
forever. Measuring across a full orbit lets the fast and slow parts average out.
Sample only two months and your predicted date can be **a year or more** out;
sample a full Mars orbit and you can get within a couple of weeks.

**The 60-day spacing is set by Venus.** Venus moves about 1.6° per day, so in 60
days it travels about 100°. That is fine. But if you stepped 120 days at a time,
Venus would move about 190° between measurements — and you would have **no way to
tell** whether it had gone 190° forwards or 170° backwards. Your code would
confidently reconstruct the wrong orbit and hand you a date that is out by more
than a year, with no warning that anything went wrong.

The rule: **the fastest planet must move less than 180° between consecutive
measurements.** For Venus that means steps shorter than about 112 days. We use 60
to leave comfortable margin. You will test this claim directly in Part 2.

### Look at the thing you are predicting

Before you leave, ask your demonstrator to fly you back to Earth's surface and
show you a Venus–Mars conjunction — a past one, so it doesn't spoil your
prediction. Watch the two planets close on each other night by night until they
sit almost on top of one another.

That is the event your code will predict the date of. It helps enormously to have
seen one.

---

# Part 2 — The Computer Lab

Here you build the model. Work in `alignment.py`; the starter file loads your CSV
and plots it, so you begin from working code.

## The function you are writing

```python
def next_alignment(days, lon_venus, lon_earth, lon_mars,
                   r_venus=None, r_earth=None, r_mars=None,
                   model="circular"):
    """Predict the next Earth-Venus-Mars alignment.

    Returns the number of days after the start date on which Venus and Mars
    next appear in the same direction as seen from Earth.
    """
```

Everything below is how to fill it in. Build it in four steps and test each step
before moving on — do not write the whole thing and then run it.

### Step 1 — Unwrap the longitudes

Your measured longitudes reset to 0 every time a planet completes an orbit, so
Venus's column looks something like `253, 350, 86, 182, ...`. Fit a straight line
to *that* and you will get nonsense.

You need the **cumulative** angle: `253, 350, 446, 542, ...`. NumPy will do it,
but it works in radians:

```python
lon_unwrapped = np.degrees(np.unwrap(np.radians(lon_venus)))
```

**Plot the unwrapped longitudes against time before going any further.** You
should see three clean straight lines with different slopes. If any line has a
kink or a step in it, either the unwrapping failed (your sampling was too coarse)
or you have a typo in your CSV. Fix it now.

This plot is also your proof that the 180° rule from Part 1 is real: try
unwrapping only every second row of your data (a 120-day step) and watch Venus's
line fall apart.

### Step 2 — Fit each orbit

**Model A — uniform circular motion.** Assume each planet sweeps around a circle
at a constant rate. Then λ is a straight line in time, and you already know how
to fit one:

```python
rate, lon_start = np.polyfit(days, lon_unwrapped, 1)   # degrees/day, degrees
```

The orbital period follows immediately: `period = 360 / rate`. Check your three
periods against the real values (225, 365 and 687 days) — this is your first
sanity check, and if Mars is badly off, your span was too short.

**Model B — allowing for a non-circular orbit.** Kepler's real orbits are
ellipses. To first order in the eccentricity *e*, the longitude is

<p align="center"><code>λ(t) = ϖ + M(t) + 2e·sin( M(t) )</code>,  where  <code>M(t) = M₀ + n·t</code></p>

Here *n* is the mean rate you just fitted, *M* is the **mean anomaly** (where the
planet *would* be if it moved uniformly), ϖ is the direction of the orbit's
closest approach to the Sun, and the `2e·sin M` term is the correction — a
periodic wobble that pushes the planet ahead of the uniform position for half the
orbit and behind for the other half. For Mars, `2e ≈ 0.19` radians, about **11°**:
far too big to ignore.

Fit *e* and ϖ by trying values and keeping the best. A grid search is
unsophisticated and completely adequate:

```python
best = None
for e in np.arange(0.0, 0.15, 0.001):
    for pi in np.arange(0.0, 360.0, 0.5):
        model = pi + M + np.degrees(2*e*np.sin(np.radians(M)))
        chi2 = np.sum((lon_unwrapped - model)**2)
        if best is None or chi2 < best[0]:
            best = (chi2, e, pi)
```

If you also measured distances, you can pin *e* down more directly, since
`r = a(1 − e·cos M)` — the distance column alone tells you the shape of the orbit,
and the longitudes then only need to supply its orientation. Either route works.

> **Keep `e` positive** in your grid. The pair (*e*, *M₀*) and the pair
> (−*e*, *M₀*+180°) describe exactly the same orbit, so if you let *e* go
> negative your fit may return a physically silly negative eccentricity that
> nevertheless predicts perfectly. Restricting to `e ≥ 0` removes the ambiguity.

### Step 3 — Get the orbital radii

To work out what Earth *sees*, you need the planets' actual positions, not just
their directions — so you need each orbit's size *a*.

If you measured distances, use the mean of your `r` column. If you didn't,
**Kepler's third law** gives it to you for free from the period you just fitted:

<p align="center"><code>a = (P / 365.25 days)<sup>2/3</sup> AU</code></p>

Both routes give the same prediction, so distances are genuinely optional. Do the
comparison and say so in your report.

> A nice cross-check: for Mars, Kepler's third law and your *measured* distance
> disagree by about 3%. That gap is not an error — it is the eccentricity, showing
> up again. Mars's distance from the Sun on the day you measured it is not the
> same as the *average* size of its orbit.

### Step 4 — Find the alignment

Now step forward in time and ask, at each moment, where Venus and Mars appear
**as seen from Earth**.

Convert each planet's orbit position to Cartesian coordinates centred on the Sun:

```python
x = r * np.cos(np.radians(lon))
y = r * np.sin(np.radians(lon))
```

Then the direction from Earth to Venus is the vector `(x_v - x_e, y_v - y_e)`, and
`np.arctan2` turns that into an angle. Do the same for Mars. The quantity you care
about is the **difference** between those two angles, wrapped into the range
−180° to +180°:

```python
def wrap180(angle):
    return (angle + 180.0) % 360.0 - 180.0
```

**An alignment is where this difference passes through zero.** Not where it is
smallest — where it *changes sign*. Look for consecutive time steps where the
difference goes from positive to negative or vice versa:

```python
crossings = np.where(delta[:-1] * delta[1:] < 0)[0]
```

Hunting for a sign change is much more robust than hunting for a minimum. A
minimum needs you to decide "how close counts as aligned?", and your answer then
depends on that arbitrary threshold — the very trap we avoided by choosing this
definition of alignment in the first place. A sign change needs no threshold at
all.

> **One trap.** The difference also jumps abruptly from +180° to −180° when the
> angles wrap around, and that looks like a sign change but isn't. Reject any
> crossing where the two values differ by more than about 90°.

Report the **first** crossing after your last measurement. Then convert
days-since-start into a real calendar date:

```python
from datetime import date, timedelta
start = date(2026, 7, 30)          # your dome session's start date
print(start + timedelta(days=float(predicted_days)))
```

## How good should your answer be?

Your prediction will be wrong, and knowing roughly *how* wrong is part of doing
this properly. From 12 measurements spanning one Mars orbit, expect:

| Model | Typical error in the predicted date |
|---|---|
| **A** — uniform circular orbits | around 10 days |
| **B** — including the eccentricity correction | 1 to 2 days |

If Model A is out by months, your span was too short or your unwrapping failed.
If Model B is *worse* than Model A, that is not necessarily a bug — see below.

## The convergence plot

This is the centrepiece figure of your report, and the most interesting thing you
will produce.

Run your prediction using only the **first *k* measurements**, for *k* = 3, 4, 5,
… 12. Plot the predicted date against *k*, for both models, on the same axes.

You should find that Model B walks steadily towards a stable answer as *k* grows
and your data covers more of Mars's orbit, while Model A flattens out at an answer
that is close but persistently off. Three things are worth writing about:

- **Model A's residual offset is physics, not noise.** It is what neglecting
  eccentricity costs you.
- **Model B is worse than Model A at small *k*.** With only half a Mars orbit
  measured, there is not enough information to pin down the eccentricity, and
  fitting it does more harm than good. A more sophisticated model is only better
  if your data can support it — one of the most useful lessons in this course.
- **Watch for accidental agreement.** At some small *k* one of your models will
  probably hit the right date almost exactly, while having Mars's orbital period
  wrong by 10%. Print the fitted period alongside each prediction so you can catch
  this. A right answer for the wrong reason is not a right answer, and spotting the
  difference is exactly the skill this project is testing.

## Verifying your prediction

Only once your code gives you a date, and you have **written it down**:

Open Stellarium on the lab machine, set the date to your prediction, and look at
Venus and Mars. If your model is good they will be within a degree or so of each
other. Step a few days either side to find the true moment of closest approach,
and compare.

One honest limitation to note in your report: your model assumes all three orbits
lie in exactly the same plane. They don't — Venus's orbit is tilted by 3.4° and
Mars's by 1.9°. So Venus and Mars never *quite* touch; they pass within a fraction
of a degree of one another. Your model can predict the **date** of the conjunction
well, but it cannot predict how close the two planets get. Be clear about which of
those two things you are claiming.

## Testing that your code is actually general

Your function should work on *any* set of measurements, not just yours. Ask your
demonstrator for a second measurement table from a different start year and run
your code on it unchanged.

Anything hard-coded — a start date, an assumed period, a hand-tuned search
window — will fail this test. Mars happens to be unusually well behaved in
2026–27, so a different epoch is a genuinely harder test than the data you
collected.

---

# Part 3 — Write-up and Presentation

## The report

The report must be written in **Markdown**, as `report.md` in your repository —
the same format you used for your essay last semester. You already know the
syntax; this time you are using it for something closer to a scientific paper, so
a few features earn their keep:

| You need | Markdown |
|---|---|
| Section headings | `## Your measurements` |
| A figure, with a caption | `![Predicted date against number of measurements used](convergence.png)` |
| A table of fitted periods | `\| Planet \| Fitted P \| Accepted P \|` |
| An equation | a fenced code block, or inline `` `λ = ϖ + M + 2e·sin M` `` |
| A caveat set apart from the text | `> Our model assumes coplanar orbits.` |

Two things to get right. **Reference your figures in the text** — write "Figure 1
shows…" and then embed it; a plot nobody points at does no work. And **commit the
`.png` files alongside `report.md`**, using relative paths like
`![...](convergence.png)`, so the figures actually render on GitHub when your
instructor opens your pull request. A report whose images are broken links reads
as an unfinished report.

Aim for about four pages rendered. Structure it like a short paper:

1. **What you set out to predict**, and your definition of alignment. Explain why
   "all three in the same direction from the Sun" was the wrong target, and what
   you used instead.
2. **Your measurements.** Show the unwrapped-longitude plot. State the three
   orbital periods you fitted and compare them to accepted values.
3. **Your model.** The equations you used, and why Model B needs the extra term.
   Keep it short — equations and a sentence each, not a derivation.
4. **Your prediction.** The date, from both models, with an uncertainty you are
   prepared to defend. Show the convergence plot and read it out in words.
5. **Verification.** What Stellarium showed, and by how much you were wrong.
6. **Error budget.** This section matters most. Rank the things limiting your
   accuracy — eccentricity, the length of your span, reading errors, the
   coplanar assumption — and say which dominates. "We were 9 days out because
   we ignored eccentricity, and here is the plot that shows it" is a far better
   report than one claiming a suspiciously perfect answer.

> **On honesty.** A report that says "our prediction was 11 days early, and we
> can show that eccentricity accounts for about 10 of those days" earns more than
> one that quietly reports the right date without explaining how. If something
> didn't work, write about it — that is a result too.

## The presentation

**Eight minutes, three or four slides, plus questions.** Everyone in the group
speaks.

Suggested shape: one slide on what you predicted and why that definition, one
slide on the convergence plot, one slide on your date versus the truth and where
the difference came from. Resist the urge to explain your code line by line —
show the physics and the figures.

Expect to be asked: *why 60-day steps?*, *what would happen with 12 measurements
over two months instead of two years?*, and *which of your two models would you
trust for a prediction ten years out?* Have answers ready.

## Marking

| Component | Weight | What earns marks |
|---|---:|---|
| Measurements and data handling | 15% | Complete, clean CSV; unwrapping plot correct; outliers found and dealt with |
| `next_alignment` implementation | 30% | Works; correctly structured; runs unchanged on a second dataset |
| Prediction and verification | 20% | A definite date, verified, with a defensible uncertainty |
| Convergence plot and error budget | 20% | Figure is clear and correct; dominant error identified and argued |
| Report and presentation | 15% | Clear, honest, readable; figures labelled; everyone contributes |

Marks are for **understanding and honesty**, not for hitting the date exactly. A
group that is 15 days out and explains precisely why will outscore a group that
is 2 days out by luck and cannot say how.

---

## Submitting your work

1. Check your program runs from a clean start:
   ```bash
   python3 alignment.py
   ```
2. Your repository should contain:
   - `measurements.csv` — your dome data
   - `alignment.py` — your model and prediction
   - `convergence.png` and `longitudes.png` — your figures
   - `report.md` — your write-up
3. **Commit** and **push**:
   ```bash
   git add .
   git commit -m "Complete Lab IX: Capstone — predicting a planetary alignment"
   git push
   ```
4. **Open a pull request** and let your instructor know you've finished.

---

You have now done, at first-year level, what planetary scientists do with far
better data and far more terms: measured a system, fitted a physical model,
extrapolated it, and then measured how much the model's simplifications cost you.
Adding the next correction term is a matter of patience, not of new ideas.
