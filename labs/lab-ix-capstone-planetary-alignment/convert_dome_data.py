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
