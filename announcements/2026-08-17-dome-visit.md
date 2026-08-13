# Semester II Major Project I — Digital Dome visit, Monday 17 August

This is the first of the capstone's two sessions and it is the only chance to
collect the data.

---

## The short version

- The Dome session is **Lab IX, week 1** -- data collection only.
- **You need no Python for this session.** You are there to measure.
- **You may work alone or in a pair** -- your choice. If you want a partner,
  agree on one **before** Monday.
- **Draw your data table before you get there.** You will not have time in the dark.
- **Be seated by 14:00.** The Dome steps through the sequence once, for the whole
  room, and it cannot be replayed for latecomers.

---

## What we are doing

You are going to build a model of the inner Solar System out of your own
measurements, and use it to predict the date of a future Venus–Mars conjunction (
the night the two planets appear almost on top of each other in our sky.)

The Dome gives you the raw data and nothing else. The modelling, the fitting and
the write-up happen on **26 October**, once you have the Python, NumPy and
plotting to handle it. That is ten weeks after the visit, which is why the
warnings about guarding your data below are not decoration.

## What you will see

The Dome puts you at the **Sun**, looking down on the plane of the ecliptic, with
the orbits of Venus, Earth and Mars in view at once. This viewpoint is the whole
reason we are going. Seen from Earth, Mars wanders backwards across the sky
several times a year and modelling that is well beyond a first-year lab. Seen
from the Sun, every planet simply marches steadily around its orbit -- and a
steady march is something you can fit a straight line to.

Over the sequence you will see:

- **A longitude grid** laid over the ecliptic plane, centred on the Sun: fine
  spokes every 10°, heavier labelled spokes every 30°, with 0° marked and the
  direction of increasing longitude indicated. The grid is fixed in space and the
  view is locked, so an angle you estimate at step 1 means the same thing at
  step 12.
- **Venus, Earth and Mars**, individually labelled or colour-coded with a key.
- **A readout** with two things on it: a clock giving the elapsed simulated time
  in **days since the session's start date**, and the **heliocentric distance in
  AU** of each of the three planets.
- **Twelve epochs**, 60 simulated days apart -- 660 days in total, near enough
  one Mars year. We hold each step for a minute and a half to two minutes, the
  demonstrator calls out the step number before each advance, and we will not
  move on until the room is ready.
- At the end, we fly back down to **Earth's surface** and step through a past
  Venus–Mars conjunction, night by night, so you can see what it is you are
  going to predict.

**There is no longitude number anywhere on the screen, and that is deliberate.**
Estimating an angle off a grid by eye is the skill this session exists to teach.
You will read each planet's angle against the graticule yourself and write it
down.

---

## Working alone or in a pair

**You can do this session on your own, or with a partner. Both are fine, and the
job is exactly the same either way.**

If you do want to work in a pair, **agree on your partner before Monday** — sort
it out during the week, not in the doorway of the Dome. We start at 14:15 and
there is no time to pair people up on the day. If you would like a partner but
have not found one by the weekend, message me and I will match you up.

One thing to be clear about, because it is the opposite of what "partner" usually
means:

> **A pair does not split the work.** You and your partner each fill in your own
> complete table -- all twelve epochs, all six numbers per epoch, measured by you.

That is not busywork. Everyone reading angles off a grid has a small personal
bias: you might consistently read a degree or two high. If the *same* person
measures every epoch, that bias is identical at each step and cancels out of the
orbital rate you fit -- it does you no harm at all. Stitch a table together from
two people's eyes and that same bias turns into scatter, and the fit gets
noticeably worse. One consistent observer beats two accurate ones here.

So what is a partner for? Keeping each other on the right step, catching a row
you skipped, comparing readings when a planet sits awkwardly between two spokes,
and being the person who still has the data if you lose yours. Useful, but not
required — if you would rather work alone, work alone.

---

## What to bring

| Bring | Why |
|---|---|
| **A data table, already drawn** | Twelve rows and seven columns. Ruling it up in a dark dome costs you the first two epochs. |
| **A pen or pencil that you can write with in low light** | The dome is dark once the show starts. |
| **Something firm to write on** | There is no desk. A clipboard, a hardcover notebook or a stiff folder. |
| **Your partner, if you are working in a pair** | Agreed on beforehand (see above). |

**You do not need a laptop, and you do not need to have written a line of Python.**

### Draw this before you arrive

```
start date: ________________________

 day | lon Venus | lon Earth | lon Mars | r Venus | r Earth | r Mars
-----+-----------+-----------+----------+---------+---------+--------
   0 |           |           |          |         |         |
  60 |           |           |          |         |         |
 120 |           |           |          |         |         |
 180 |           |           |          |         |         |
 240 |           |           |          |         |         |
 300 |           |           |          |         |         |
 360 |           |           |          |         |         |
 420 |           |           |          |         |         |
 480 |           |           |          |         |         |
 540 |           |           |          |         |         |
 600 |           |           |          |         |         |
 660 |           |           |          |         |         |
```

The three longitudes you estimate off the grid; the three distances you copy off
the readout. Six numbers per epoch, twelve times.

> **Write down the start date.** It is announced at the very beginning and left
> up. Every one of your measurements is "so many days after the start date" -- a
> table without it is a table of numbers that mean nothing in October.

---

## After the session

**Commit your table to your capstone repository in the same week.** Type it up,
push it, done. You probably will not touch it again until 26 October, and a data file that
goes missing over ten weeks cannot be re-measured.

A photograph of your handwritten page can also be helpful. 

