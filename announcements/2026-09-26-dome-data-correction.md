# Lab IX capstone — a correction to your Dome data, and what you need to add

If you were at the Digital Dome on 17 August, please read this before 26 October.

---

## What went wrong

The Dome was set up with the viewpoint centred on **Earth**, not the Sun, for
the whole data-collection sequence. So the table you filled in has:

- the day count, as planned
- Venus's and Mars's angle off the grid — but this is the angle **as seen from
  Earth**, not from the Sun
- no distances — the AU panel could not be shown that day, so those three
  columns are empty

This is not a small difference. The reason the session put you at the Sun in
the first place is that a planet's angle *from the Sun* advances steadily, so
you can fit a straight line to it. A planet's angle *from Earth* does not —
Mars visibly loops backwards for weeks around opposition, and Venus does not
go around at all; it just swings back and forth within about 46° of the Sun's
direction. Fitting a straight line to what you actually wrote down will not
give you an orbit.

The good news: what you measured is not wasted. Venus's and Mars's angle from
Earth, combined with a bit of geometry and a short table of extra numbers
below, gets you back to heliocentric longitude — the thing you were meant to
measure. You still do the conversion yourselves; we are only supplying the
piece the broken viewpoint didn't let you read.

## The geometry

Put the Sun at the origin. Earth sits at heliocentric longitude λ_E and
distance r_E (both in the table below). A planet sits somewhere on its own
orbit, at heliocentric distance r_P (also below) — you don't know its
heliocentric longitude yet, but you do know the direction you saw it in from
Earth: λ_geo, the number you wrote down.

So the planet lies along the ray from Earth in direction λ_geo, at some
unknown distance *d* from Earth, **and** it lies at distance r_P from the Sun.
Writing that out (Sun–Earth–planet as a triangle) gives a quadratic in *d*:

```
d² + 2 r_E cos(λ_geo − λ_E) d + (r_E² − r_P²) = 0
```

Solve it, keep the positive root(s), then

```
x = r_E cos(λ_E) + d cos(λ_geo)
y = r_E sin(λ_E) + d sin(λ_geo)
λ_helio = atan2(y, x)
```

### Worked example — a planet farther from the Sun than Earth is

None of these numbers are from your data. Say Earth is at λ_E = 40°,
r_E = 1.00 AU, and you're converting a planet with r_P = 1.60 AU seen at
λ_geo = 100°.

```
Δ = λ_geo − λ_E = 60°
d² + 2(1.00)cos(60°) d + (1.00² − 1.60²) = 0
d² + d − 1.56 = 0
d = [−1 ± √7.24] / 2  →  d ≈ 0.846  or  d ≈ −1.846
```

Only the positive root is physical: d ≈ 0.846 AU. Then

```
x = 1.00 cos40° + 0.846 cos100° ≈ 0.619
y = 1.00 sin40° + 0.846 sin100° ≈ 1.476
λ_helio = atan2(1.476, 0.619) ≈ 67.2°
```

(Check: √(0.619² + 1.476²) ≈ 1.60 — matches r_P, as it should.)

This is the case for **Mars**: because r_Mars is always bigger than r_Earth,
the quadratic only ever has one positive root. One measurement, one answer.

### Worked example — a planet closer to the Sun than Earth is

Again, invented numbers. Earth at λ_E = 0°, r_E = 1.00 AU, converting a planet
with r_P = 0.70 AU seen at λ_geo = 200°.

```
Δ = 200°
d² + 2(1.00)cos(200°) d + (1.00² − 0.70²) = 0
d² − 1.879 d + 0.51 = 0
d ≈ 0.329  or  d ≈ 1.551
```

**Both roots are positive.** Working each through to λ_helio:

- d ≈ 0.329 AU → λ_helio ≈ 351°
- d ≈ 1.551 AU → λ_helio ≈ 229°

Two genuinely different answers, ~120° apart, from the same single
measurement. This isn't a mistake in the algebra — geometrically, a ray from
Earth generally crosses a smaller circle (Venus's orbit) twice, and a single
angle can't tell you which crossing is real.

This is the case for **Venus**: r_Venus is smaller than r_Earth, so most of
your twelve epochs will have two candidate longitudes, and you have to choose
one. **Use continuity**: pick whichever root sits closer to the value you
picked at the previous epoch — the real Venus moves smoothly from one epoch to
the next, 60 days apart, so its true longitude can't jump by 120° between
consecutive readings. The two roots merge into one only at the epoch(s) where
Venus sits at its largest elongation from the Sun; everywhere else, continuity
should make the choice obvious once you've picked a starting point.

## The extra data

These are Earth's heliocentric longitude and the three heliocentric distances
for your twelve epochs — the numbers the AU panel should have shown you on
the day. They do **not** include Venus's or Mars's heliocentric longitude:
that's still yours to work out, the same as it always was.

```
# days_since_start, lon_earth, r_venus, r_earth, r_mars
0,    323.76, 0.7276, 1.0125, 1.5003
60,    22.28, 0.7253, 0.9971, 1.5763
120,   82.64, 0.7187, 0.9843, 1.6351
180,  143.67, 0.7224, 0.9872, 1.6641
240,  203.46, 0.7282, 1.0028, 1.6582
300,  261.42, 0.7233, 1.0155, 1.6182
360,  318.71, 0.7185, 1.0134, 1.5519
420,   17.07, 0.7245, 0.9985, 1.4743
480,   77.29, 0.7279, 0.9849, 1.4091
540,  138.35, 0.7213, 0.9863, 1.3812
600,  198.29, 0.7192, 1.0012, 1.4035
660,  256.39, 0.7263, 1.0149, 1.4656
```

Longitudes are in degrees, distances in AU, matched to your own day count from
17 August.

## What to actually do with this

Keep your own handwritten λ_Venus and λ_Mars readings exactly as you recorded
them — don't try to correct them by eye. The conversion above is an extra step
you run once you have Python, alongside the rest of the Lab IX modelling: for
each of your twelve epochs, take your λ_geo reading, the matching r_E and
λ_earth from the table, and the r_venus or r_mars for that row, and solve for
λ_helio as shown. That gives you the heliocentric longitude table the Dome was
meant to hand you directly — from there, the rest of the capstone (fitting a
rate, predicting the conjunction) is unchanged.

If anything here doesn't line up with what you wrote down on the day —
in particular if your table is missing a row, or you're unsure which of
Venus's or Mars's columns you actually measured — get in touch before 26
October rather than guessing.
