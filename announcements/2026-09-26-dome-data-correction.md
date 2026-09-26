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
measure.

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
longitudes — anywhere from a few degrees to most of a half-circle apart — can
both be geometrically valid for the same measurement. The two candidates
merge into one only at the epoch(s) where Venus sits at its largest elongation
from the Sun.

**Picking the right one is not as simple as "closest to last time."** Venus
moves roughly 1.6° per day, so across a 60-day step it moves roughly 96° —
often *more* than the gap between the two candidates. Comparing each new
candidate to the raw previous value routinely picks the wrong one. What
works instead is comparing each candidate to where Venus should *roughly* be,
given the previous value and that known rate of motion, and at the very first
epoch — where there is no previous value yet — trying both candidates as the
starting point and keeping whichever choice stays consistent with itself
across the whole run.

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

# Roughly how fast each planet moves round the Sun, in degrees per day.
# Venus's own orbital period is about 225 days and Mars's about 687 days,
# so these are just 360 divided by that. They only need to be roughly
# right -- they're used to guess which of two candidate positions is the
# real one, not to fit anything.
VENUS_APPROX_RATE_DEG_PER_DAY = 360.0 / 225.0
MARS_APPROX_RATE_DEG_PER_DAY = 360.0 / 687.0


def earth_heliocentric_xy(earth_longitude_deg, earth_distance_au):
    """Earth's (x, y) position in the heliocentric frame, Sun at the origin."""
    angle = math.radians(earth_longitude_deg)
    return earth_distance_au * math.cos(angle), earth_distance_au * math.sin(angle)


def earth_planet_distance_candidates(geocentric_longitude_deg, earth_longitude_deg,
                                      earth_distance_au, planet_distance_au):
    """
    Solve the Sun-Earth-planet triangle for the Earth-planet distance.

    Returns (candidates, warning). candidates is a list of the physically
    valid (positive) solutions for the distance along the line of sight:
    one for a planet farther from the Sun than Earth (e.g. Mars), or one or
    two for a planet closer to the Sun than Earth (e.g. Venus), depending on
    whether the sightline actually crosses the planet's orbit.

    A planet closer to the Sun than Earth can never appear, as seen from
    Earth, more than max_elongation = asin(planet_distance_au / earth_distance_au)
    away from the Sun's own direction. If the reading implies a wider angle
    than that -- almost always a transcription or reading error -- there is
    no exact solution. warning is then a message saying so, and candidates
    holds the single closest point instead of failing outright; otherwise
    warning is None.
    """
    longitude_offset_deg = geocentric_longitude_deg - earth_longitude_deg
    longitude_offset_rad = math.radians(longitude_offset_deg)
    linear_coefficient = 2 * earth_distance_au * math.cos(longitude_offset_rad)
    constant_term = earth_distance_au ** 2 - planet_distance_au ** 2
    discriminant = linear_coefficient ** 2 - 4 * constant_term

    warning = None
    if discriminant < 0:
        max_elongation_deg = math.degrees(
            math.asin(min(1.0, planet_distance_au / earth_distance_au))
        )
        implied_elongation_deg = abs(longitude_offset_deg % 360 - 180)
        warning = (
            f"reading implies the planet is {implied_elongation_deg - max_elongation_deg:.1f} deg "
            f"beyond its {max_elongation_deg:.1f} deg maximum possible elongation -- "
            "treating it as the nearest point on the known orbit; check this row "
            "for a transcription error"
        )
        discriminant = 0.0

    sqrt_discriminant = math.sqrt(discriminant)
    roots = [
        (-linear_coefficient + sqrt_discriminant) / 2,
        (-linear_coefficient - sqrt_discriminant) / 2,
    ]
    candidates = [distance for distance in roots if distance > 0]
    return candidates, warning


def heliocentric_longitude_deg(geocentric_longitude_deg, earth_x, earth_y, distance_au):
    """Heliocentric longitude of a point a given distance along the sightline from Earth."""
    angle = math.radians(geocentric_longitude_deg)
    planet_x = earth_x + distance_au * math.cos(angle)
    planet_y = earth_y + distance_au * math.sin(angle)
    return math.degrees(math.atan2(planet_y, planet_x)) % 360


def closest_to(candidates, target_deg):
    """Whichever candidate longitude is closest to target_deg, wrapping at 360 degrees."""
    def angular_distance(first_deg, second_deg):
        difference = abs(first_deg - second_deg)
        return min(difference, 360 - difference)
    return min(candidates, key=lambda candidate: angular_distance(candidate, target_deg))


def predicted_longitude_deg(previous_deg, approx_rate_deg_per_day, elapsed_days):
    """Where the planet should be roughly, given its last position and its known rate."""
    return (previous_deg + approx_rate_deg_per_day * elapsed_days) % 360


def candidate_longitudes_for_epoch(geocentric_longitude_deg, earth_longitude_deg,
                                    earth_distance_au, planet_distance_au):
    """The heliocentric longitude candidate(s) for a single epoch, plus any warning."""
    earth_x, earth_y = earth_heliocentric_xy(earth_longitude_deg, earth_distance_au)
    distances, warning = earth_planet_distance_candidates(
        geocentric_longitude_deg, earth_longitude_deg, earth_distance_au, planet_distance_au
    )
    longitudes = [
        heliocentric_longitude_deg(geocentric_longitude_deg, earth_x, earth_y, distance)
        for distance in distances
    ]
    return longitudes, warning


def build_path(geocentric_longitudes_deg, earth_longitudes_deg, earth_distances_au,
               planet_distances_au, days_since_start, approx_rate_deg_per_day,
               first_choice_index):
    """
    Walk the whole series once, choosing a candidate at every epoch after
    the first by picking whichever is closest to where the planet should
    roughly be, given its previous position and its known rate of motion.

    At the first epoch there is nothing to compare to, so first_choice_index
    picks which candidate to start from when there are two (0 or 1; ignored
    when there is only one). Returns (chosen_longitudes, total_surprise,
    warnings), where total_surprise is the sum, over every epoch after the
    first, of how far the chosen candidate was from the prediction -- a
    measure of how well this starting choice held together.
    """
    chosen_longitudes = []
    warnings = []
    total_surprise = 0.0
    previous_longitude = None
    previous_day = None

    for day, lon_geo, lon_earth, r_earth, r_planet in zip(
        days_since_start, geocentric_longitudes_deg, earth_longitudes_deg,
        earth_distances_au, planet_distances_au
    ):
        candidates, warning = candidate_longitudes_for_epoch(lon_geo, lon_earth, r_earth, r_planet)
        if warning is not None:
            warnings.append(f"day {day}: {warning}")

        if previous_longitude is None:
            chosen = candidates[first_choice_index] if len(candidates) > 1 else candidates[0]
        elif len(candidates) == 1:
            chosen = candidates[0]
        else:
            prediction = predicted_longitude_deg(
                previous_longitude, approx_rate_deg_per_day, day - previous_day
            )
            chosen = closest_to(candidates, prediction)
            difference = abs(chosen - prediction)
            total_surprise += min(difference, 360 - difference)

        chosen_longitudes.append(chosen)
        previous_longitude, previous_day = chosen, day

    return chosen_longitudes, total_surprise, warnings


def convert_series(geocentric_longitudes_deg, earth_longitudes_deg, earth_distances_au,
                    planet_distances_au, days_since_start, approx_rate_deg_per_day):
    """
    Convert a whole series of geocentric readings to heliocentric longitude.

    For a planet closer to the Sun than Earth (e.g. Venus), a single epoch
    can have two valid candidates, and the first epoch has no earlier value
    to compare to -- so this tries starting from each candidate at the first
    epoch, and keeps whichever choice stays closest to its own predictions
    across the whole series. (When every epoch has only one candidate, both
    attempts are identical, so this is safe to run either way.)
    """
    first_attempt = build_path(
        geocentric_longitudes_deg, earth_longitudes_deg, earth_distances_au,
        planet_distances_au, days_since_start, approx_rate_deg_per_day, first_choice_index=0,
    )
    second_attempt = build_path(
        geocentric_longitudes_deg, earth_longitudes_deg, earth_distances_au,
        planet_distances_au, days_since_start, approx_rate_deg_per_day, first_choice_index=1,
    )
    chosen_longitudes, total_surprise, warnings = min(
        first_attempt, second_attempt, key=lambda attempt: attempt[1]
    )
    return chosen_longitudes, warnings


def main():
    # Replace these two lists with your own twelve readings, in the same
    # order as DAYS_SINCE_START above. The numbers below are made up, just
    # to show the script running end to end -- they are not real Dome data.
    example_venus_geocentric_deg = [
        106.8, 181.4, 259.0, 337.3, 53.8, 124.9,
        171.1, 154.1, 214.0, 289.4, 6.5, 82.9,
    ]
    example_mars_geocentric_deg = [
        52.4, 65.8, 52.3, 64.3, 95.0, 131.3,
        170.1, 210.8, 253.0, 295.9, 337.7, 16.7,
    ]

    venus_helio_deg, venus_warnings = convert_series(
        example_venus_geocentric_deg, EARTH_LONGITUDE_DEG,
        EARTH_DISTANCE_AU, VENUS_DISTANCE_AU, DAYS_SINCE_START,
        VENUS_APPROX_RATE_DEG_PER_DAY,
    )
    mars_helio_deg, mars_warnings = convert_series(
        example_mars_geocentric_deg, EARTH_LONGITUDE_DEG,
        EARTH_DISTANCE_AU, MARS_DISTANCE_AU, DAYS_SINCE_START,
        MARS_APPROX_RATE_DEG_PER_DAY,
    )

    print(f"{'day':>5}  {'venus (helio)':>14}  {'mars (helio)':>13}")
    for day, venus_lon, mars_lon in zip(DAYS_SINCE_START, venus_helio_deg, mars_helio_deg):
        print(f"{day:5d}  {venus_lon:14.2f}  {mars_lon:13.2f}")

    for warning in venus_warnings + mars_warnings:
        print(f"venus/mars warning -- {warning}")


if __name__ == "__main__":
    main()
```

Running it as it stands (with the made-up example readings baked in, **not**
your data) prints:

```
  day   venus (helio)   mars (helio)
    0           50.01           9.97
   60          152.06          39.98
  120          254.01          70.00
  180          356.09          99.97
  240           97.88         130.00
  300          199.93         159.98
  360          302.03         189.98
  420           44.05         220.05
  480          145.91         250.00
  540          247.96         280.08
  600          349.97         310.05
  660           92.02         339.99
```

Notice `candidate_longitudes_for_epoch` returns **two** candidates at every
one of these example epochs for Venus, yet the printed longitudes still climb
steadily. That's `convert_series` doing two things: trying both candidates as
the starting point at day 0 (since there's nothing earlier to compare
against), and picking whichever candidate at each later epoch is closest to
where Venus should roughly be, given its previous position and its known
~1.6°/day rate — not closest to the raw previous value, which is not the same
thing once a single step covers most of Venus's ~46° maximum elongation swing.
It also won't crash if a reading turns out to be very slightly beyond what's
geometrically possible (a small mismatch is common with a hand-read angle);
it prints a warning and uses the nearest point on the known orbit instead.

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

## One more fix, unrelated to the above: your Part 2 instructions

Separately from the geocentric/heliocentric mix-up, two code snippets in your
capstone README used single-letter or confusable variable names: the
eccentricity grid search (Part 2, Step 2, Model B) used `e` and `pi` as loop
variable names — `pi` in particular is a bad name for anything other than the
constant 3.14159… — and the Cartesian-conversion snippet (Step 4) used
`x`/`y`/`r`. Both have been renamed (to `eccentricity`/
`pericenter_longitude_deg`, and `planet_x`/`planet_y`/`radius_au`, in the
template repository your own was generated from) and pushed directly to your
own capstone repository's README, since that repository was generated on 14
September — before this fix was made, and a template fix afterwards doesn't
reach a repository already generated from it. No behaviour changed, only
names. `convert_dome_data.py` has also been added to your repository directly,
so you don't need to copy it from this announcement.
