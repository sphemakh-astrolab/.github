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

For a planet farther from the Sun than Earth (Mars), that quadratic always has
exactly one positive root — one measurement, one answer. For a planet closer
to the Sun than Earth (Venus), it can have **two** positive roots: a ray from
Earth generally crosses Venus's smaller orbit twice, and a single angle can't
tell you which crossing is real. Two genuinely different heliocentric
longitudes, tens of degrees apart, can both be geometrically valid for the
same measurement. The fix is continuity: of the two candidates, keep whichever
is closer to the value you chose at the previous epoch, since Venus can't jump
between them in a single 60-day step. The two candidates merge into one only
at the epoch(s) where Venus sits at its largest elongation from the Sun.

## The code

Since you're not the ones who introduced this problem, here is a script that
does the conversion, rather than another worked example for you to reproduce
by hand. It implements exactly the geometry above: one function per step,
each with a one-line docstring saying what it returns, and a `main()` that
wires them together — this is also meant as a template for how to structure
the rest of your capstone scripts.

**[`convert_dome_data.py`](https://github.com/sphemakh-astrolab/.github/blob/main/labs/lab-ix-capstone-planetary-alignment/convert_dome_data.py)**
— this lives here rather than in your capstone template repo, since a fix
made now wouldn't reach a template repo already generated for you.

```python
"""
Convert Dome geocentric longitude readings to heliocentric longitude.

Background: the 17 August Dome session ended up viewed from Earth rather
than the Sun, so what you measured for Venus and Mars is each planet's
ecliptic longitude *as seen from Earth* (geocentric), not from the Sun
(heliocentric). This script converts one to the other, using Earth's own
heliocentric position -- which the broken viewpoint could not show you
directly, but which is known from the same reference data the Dome session
was set up from.

This file is also meant as a template for how to structure your own
capstone scripts: one function per well-defined step, a docstring saying
what each function returns, and a main() that reads the data, calls the
functions in order, and reports the result.
"""

import math


# Earth's heliocentric longitude (degrees) and the three heliocentric
# distances (AU), for the same twelve epochs you measured at the Dome.
# These come from the same reference data the session was set up from, and
# were not something the broken viewpoint could show you.
DAYS_SINCE_START = [0, 60, 120, 180, 240, 300, 360, 420, 480, 540, 600, 660]
EARTH_LONGITUDE_DEG = [323.76, 22.28, 82.64, 143.67, 203.46, 261.42,
                       318.71, 17.07, 77.29, 138.35, 198.29, 256.39]
VENUS_DISTANCE_AU = [0.7276, 0.7253, 0.7187, 0.7224, 0.7282, 0.7233,
                      0.7185, 0.7245, 0.7279, 0.7213, 0.7192, 0.7263]
EARTH_DISTANCE_AU = [1.0125, 0.9971, 0.9843, 0.9872, 1.0028, 1.0155,
                      1.0134, 0.9985, 0.9849, 0.9863, 1.0012, 1.0149]
MARS_DISTANCE_AU = [1.5003, 1.5763, 1.6351, 1.6641, 1.6582, 1.6182,
                     1.5519, 1.4743, 1.4091, 1.3812, 1.4035, 1.4656]


def earth_heliocentric_xy(earth_longitude_deg, earth_distance_au):
    """Earth's (x, y) position in the heliocentric frame, Sun at the origin."""
    angle = math.radians(earth_longitude_deg)
    return earth_distance_au * math.cos(angle), earth_distance_au * math.sin(angle)


def earth_planet_distance_candidates(geocentric_longitude_deg, earth_longitude_deg,
                                      earth_distance_au, planet_distance_au):
    """
    Solve the Sun-Earth-planet triangle for the Earth-planet distance.

    Returns a list of the physically valid (positive) solutions for the
    distance along the line of sight: one for a planet farther from the Sun
    than Earth (e.g. Mars), or zero, one or two for a planet closer to the
    Sun than Earth (e.g. Venus), depending on whether the sightline actually
    crosses the planet's orbit.
    """
    elongation = math.radians(geocentric_longitude_deg - earth_longitude_deg)
    b = 2 * earth_distance_au * math.cos(elongation)
    c = earth_distance_au ** 2 - planet_distance_au ** 2
    discriminant = b ** 2 - 4 * c
    if discriminant < 0:
        return []
    sqrt_discriminant = math.sqrt(discriminant)
    roots = [(-b + sqrt_discriminant) / 2, (-b - sqrt_discriminant) / 2]
    return [d for d in roots if d > 0]


def heliocentric_longitude_deg(geocentric_longitude_deg, earth_x, earth_y, distance_au):
    """Heliocentric longitude of a point a given distance along the sightline from Earth."""
    angle = math.radians(geocentric_longitude_deg)
    x = earth_x + distance_au * math.cos(angle)
    y = earth_y + distance_au * math.sin(angle)
    return math.degrees(math.atan2(y, x)) % 360


def closest_to(candidates, target_deg):
    """Whichever candidate longitude is closest to target_deg, wrapping at 360 degrees."""
    def angular_distance(a, b):
        return min(abs(a - b), 360 - abs(a - b))
    return min(candidates, key=lambda candidate: angular_distance(candidate, target_deg))


def convert_series(geocentric_longitudes_deg, earth_longitudes_deg,
                    earth_distances_au, planet_distances_au):
    """
    Convert a whole series of geocentric readings to heliocentric longitude.

    For a planet closer to the Sun than Earth (e.g. Venus), a single epoch
    can have two valid solutions. We keep whichever is closest to the
    previous epoch's chosen value, since the true motion is smooth from one
    60-day step to the next.
    """
    results = []
    previous = None
    for lon_geo, lon_earth, r_earth, r_planet in zip(
        geocentric_longitudes_deg, earth_longitudes_deg,
        earth_distances_au, planet_distances_au
    ):
        earth_x, earth_y = earth_heliocentric_xy(lon_earth, r_earth)
        distances = earth_planet_distance_candidates(lon_geo, lon_earth, r_earth, r_planet)
        candidates = [
            heliocentric_longitude_deg(lon_geo, earth_x, earth_y, d)
            for d in distances
        ]

        if len(candidates) == 1 or previous is None:
            chosen = candidates[0]
        else:
            chosen = closest_to(candidates, previous)

        results.append(chosen)
        previous = chosen
    return results


def main():
    # Replace these two lists with your own twelve readings, in the same
    # order as DAYS_SINCE_START above. The numbers below are made up, just
    # to show the script running end to end -- they are not real Dome data.
    example_venus_geocentric_deg = [
        173.8, 182.3, 297.6, 298.7, 43.5, 46.4,
        163.7, 182.1, 267.3, 288.4, 33.3, 66.4,
    ]
    example_mars_geocentric_deg = [
        40.0, 95.0, 150.0, 200.0, 250.0, 300.0,
        350.0, 40.0, 90.0, 140.0, 190.0, 240.0,
    ]

    venus_helio_deg = convert_series(
        example_venus_geocentric_deg, EARTH_LONGITUDE_DEG,
        EARTH_DISTANCE_AU, VENUS_DISTANCE_AU,
    )
    mars_helio_deg = convert_series(
        example_mars_geocentric_deg, EARTH_LONGITUDE_DEG,
        EARTH_DISTANCE_AU, MARS_DISTANCE_AU,
    )

    print(f"{'day':>5}  {'venus (helio)':>14}  {'mars (helio)':>13}")
    for day, venus_lon, mars_lon in zip(DAYS_SINCE_START, venus_helio_deg, mars_helio_deg):
        print(f"{day:5d}  {venus_lon:14.2f}  {mars_lon:13.2f}")


if __name__ == "__main__":
    main()
```

Running it as it stands (with the made-up example readings baked in, **not**
your data) prints:

```
  day   venus (helio)   mars (helio)
    0          217.96         359.04
   60          154.28          57.84
  120           65.90         116.25
  180          153.93         170.41
  240          195.34         223.96
  300          280.08         276.96
  360          307.13         330.17
  420           22.96          24.70
  480           73.70          81.15
  540          151.45         138.82
  600          192.17         195.90
  660          260.43         251.27
```

Notice `earth_planet_distance_candidates` returns **two** candidates at every
one of these example epochs for Venus, yet the printed longitudes still move
smoothly — that's `closest_to` doing the continuity resolution described
above, epoch by epoch, not a coincidence of these particular made-up numbers.

To use it on your own data: replace `example_venus_geocentric_deg` and
`example_mars_geocentric_deg` in `main()` with your own twelve readings, in
the same day order, and re-run.

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

## A second estimate, from everyone's data pooled together

On 26 October you'll produce two conjunction estimates, not one: your own,
from your own twelve epochs as above, and a second from **all** students'
raw readings pooled together, to compare against it.

**[Submit your raw geocentric readings here](https://github.com/sphemakh-astrolab/.github/issues/new?template=dome-measurements.yml)**
— the twelve epochs you actually wrote down at the Dome, not the converted
heliocentric values. One issue per person, even if you worked in a pair. The
conversion above will be applied once, the same way, to the whole pooled set,
so it needs your raw numbers, not your own converted ones.
