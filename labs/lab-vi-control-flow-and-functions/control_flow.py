# Lab VI: Control Flow and Functions in Python
# Programming Essentials for Astronomy I - Python
#
# Fill in the TODOs below. Run with:
#     python3 control_flow.py

# --- Part A: making decisions ----------------------------------------------

# Exercise 1: classify a star by temperature (O B A F G K M)
temperature = 5778   # the Sun, in kelvin
if temperature >= 30000:
    print("Class O")
elif temperature >= 10000:
    print("Class B")
# TODO: add elif branches for A (>=7500), F (>=6000), G (>=5200), K (>=3700)
else:
    print("Class M")


# Exercise 2: boolean logic -- can you see it?
magnitude = 1.25
naked_eye = magnitude < 6.0
city_visible = magnitude < 3.0
# TODO: print whether the star is visible from a city (naked_eye AND city_visible)


# --- Part B: repeating things ----------------------------------------------

# Exercise 3: a for loop with range()
print("--- Light-travel table ---")
for distance in range(1, 11):
    year_left = 2026 - distance
    print(f"{distance} ly  ->  light left in {year_left}")
# TODO: try range(0, 21, 5) and see what the third number does.


# Exercise 4: a while loop
brightness = 100.0
steps = 0
while brightness >= 1.0:
    brightness = brightness / 2
    steps = steps + 1
# TODO: print how many steps it took to drop below 1.


# --- Part C: functions -----------------------------------------------------

# Exercise 5: turn the classifier into a function that RETURNS the letter
def spectral_class(temperature):
    if temperature >= 30000:
        return "O"
    elif temperature >= 10000:
        return "B"
    # TODO: add A, F, G, K branches
    else:
        return "M"

print(spectral_class(5778))   # expect G once you finish the branches
print(spectral_class(25000))  # expect B


# Exercise 6: a function with a default argument
def light_left_year(distance_ly, now=2026):
    return now - distance_ly

print(light_left_year(8.6))         # uses now = 2026
print(light_left_year(8.6, 2000))   # overrides now


# --- Optional extension ----------------------------------------------------
# TODO: loop over temperatures 3000..40000 in steps of 1000 and print each
#       temperature next to spectral_class(temperature).
