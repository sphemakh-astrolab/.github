# Lab V: Introduction to Python — Basics, Control Flow and Functions

**Programming Essentials for Astronomy I — Python**

Welcome to Python! For the rest of the course we switch from C++ to
[Python](https://www.python.org), the language we'll use to do real scientific
data analysis. The good news: everything you learned in C++ — variables, types,
arithmetic, input and output, decisions, loops and functions — still applies.
Python just lets you express it with a lot less ceremony.

This lab is deliberately gentle. We take calculations you already know how to do
in C++ and re-do them in Python, so you can *feel* the differences, then bring
back **conditionals, loops and functions** in their Python form.

The one genuinely new habit Python demands is **indentation**: instead of curly
braces `{ }`, Python uses the *spaces at the start of a line* to decide what is
"inside" an `if` or a loop or a function. Line up your code carefully and it
reads beautifully; get it wrong and Python will tell you.

---

## How this lab runs

This lab spans **two sessions**, with one submission at the end.

| | Session | You work on | Starter file |
|---|---|---|---|
| **Week 1** | Mini-lecture, then start the lab | Parts A–C, Exercises 1–6 | [`intro_to_python.py`](intro_to_python.py) |
| **Week 2** | Continue and finish | Parts D–F, Exercises 7–12 | [`control_flow.py`](control_flow.py) |

**Submit everything by midnight on the day of the second session.** See
[Submitting your work](#submitting-your-work) at the end.

---

## Learning goals

By the end of this lab you should be able to:

1. **Run Python** two ways: interactively (the REPL) and by running a `.py` file.
2. Create **variables without declaring their type**, and recognise Python's
   basic types: `int`, `float`, `str`, `bool`.
3. Use **`print()`** to show results and **`input()`** to read from the user.
4. Do **arithmetic**, including the difference between `/` (true division) and
   `//` (integer division), and the power operator `**`.
5. Format output cleanly with **f-strings**.
6. Make decisions with **`if` / `elif` / `else`**, combining conditions with the
   comparison (`==`, `!=`, `<`, `>=`, ...) and boolean (`and`, `or`, `not`)
   operators.
7. Repeat work with a **`for` loop** over `range(...)` and with a **`while`** loop.
8. Use **indentation** correctly to mark out blocks of code.
9. Define your own **functions** with `def`, including parameters, `return`
   values, and default arguments.

## Before you start

- Work in your Ubuntu (WSL) terminal, with this repository open in **VSCode**.
- Check Python is installed:
  ```bash
  python3 --version
  ```
- Two starter files are provided, one per session. Both already run — try the
  first now:
  ```bash
  python3 intro_to_python.py
  ```

> **The big difference from C++:** there is **no compile step**. In C++ you ran
> `g++ program.cpp -o program` and then `./program`. In Python you just run the
> source file directly with `python3 intro_to_python.py`. Change the file, run it
> again — that's the whole loop.

You can also try the **REPL** (Read–Eval–Print Loop), an interactive Python
prompt. Type `python3` on its own, then try `2 + 2` and press Enter. Type
`exit()` to leave.

---

## Python vs C++ at a glance

| Idea                 | C++                                  | Python                        |
|----------------------|--------------------------------------|-------------------------------|
| Declaring a variable | `double distance = 8.6;`             | `distance = 8.6`              |
| No type needed       | you must write the type              | Python figures it out         |
| Line endings         | every statement ends in `;`          | no semicolons                 |
| Printing             | `std::cout << x << std::endl;`       | `print(x)`                    |
| Comments             | `// like this`                       | `# like this`                 |
| Blocks               | `{ curly braces }`                   | **indentation** + a colon `:` |
| Power (e.g. r³)      | `r * r * r` (no built-in operator)   | `r ** 3`                      |
| If / else            | `if (x > 0) { ... } else { ... }`    | `if x > 0:` / `else:`         |
| "else if"            | `else if (...)`                      | `elif ...:`                   |
| For loop             | `for (int i = 0; i < 10; i++)`       | `for i in range(10):`         |
| While loop           | `while (x > 0) { ... }`              | `while x > 0:`                |
| Function             | `int f(int n) { return n; }`         | `def f(n):` / `return n`      |
| And / or / not       | `&&` / `\|\|` / `!`                  | `and` / `or` / `not`          |

Notice the pattern: a line that opens a block **ends in a colon `:`**, and
everything inside it is **indented** (4 spaces is standard).

---

# Week 1 — Python basics

Work in [`intro_to_python.py`](intro_to_python.py).

## Part A — First steps

### Exercise 1: Hello, Universe

Use `print()` to display a short greeting, your name, and your favourite
celestial object, each on its own line.

### Exercise 2: Variables and types

We'll describe the star **Sirius** (the brightest star in the night sky, which
you met in Lab IV). Create four variables — one of each basic type:

```python
name = "Sirius"          # str  — text
distance_ly = 8.6        # float — a number with a decimal point
num_planets = 0          # int  — a whole number
naked_eye_visible = True # bool — True or False
```

Notice you did **not** have to write `std::string`, `double`, or `int` — Python
reads the value and picks the type for you. Confirm this by printing the type of
each, e.g.:

```python
print(name, "has type", type(name))
```

---

## Part B — Arithmetic with astronomy

### Exercise 3: Unit conversions

Astronomers measure distances in different units. Starting from Sirius'
distance of `8.6` light-years:

- Convert to **parsecs** (1 parsec ≈ 3.26 light-years).
- Convert to **kilometres** (1 light-year ≈ 9.46 × 10¹² km — in Python you can
  write this as `9.46e12`).

Print both results using **f-strings**, which let you drop a variable straight
into a string:

```python
distance_pc = distance_ly / 3.26
print(f"Sirius is {distance_pc} parsecs away.")
```

### Exercise 4: We see the past

The light reaching your eye from Sirius left the star `8.6` years ago. Compute
and print the calendar year in which that light *left* Sirius (use `2026` as
"now").

Then try the difference between the two division operators and print both:

```python
print(8.6 / 3)    # true division -> a float
print(8 // 3)     # integer division -> throws away the remainder
```

### Exercise 5: The C++ contrast — the power operator

In C++, to cube a number you had to multiply it out (`r * r * r`), because C++
has no power operator. Python has `**`.

Compute the **volume of a star** treated as a sphere,
V = (4/3) · π · r³, for the Sun (radius ≈ `696000` km):

```python
pi = 3.14159
radius_km = 696000
volume = (4 / 3) * pi * radius_km ** 3
print(f"The Sun's volume is about {volume:.3e} cubic km.")
```

The `:.3e` inside the f-string prints the number in scientific notation with 3
decimal places — handy for the huge and tiny numbers we meet in astronomy.

---

## Part C — Talking to the user

### Exercise 6: Reading input

Use `input()` to ask the user for a star's distance in light-years, then print
that distance converted to parsecs.

```python
text = input("Enter a distance in light-years: ")
distance_ly = float(text)   # input() ALWAYS gives text — convert it!
print(f"That is {distance_ly / 3.26:.2f} parsecs.")
```

> **Watch out:** `input()` always returns a **string**, even if the user types a
> number. If you forget to convert it with `float(...)` or `int(...)`, Python
> will try to do maths on text and complain.

### Optional extension for Week 1

Python has a `math` module with things like π and logarithms:

```python
import math
print(math.pi)
print(math.log10(100))   # -> 2.0
```

Use `math` to compute the **distance modulus** of a star,
μ = 5 · log₁₀(d) − 5, where `d` is the distance in **parsecs**. Try it for
Sirius (≈ 2.64 pc). (We'll use logarithms like this a lot when we get to real
brightness measurements.)

---

# Week 2 — Control flow and functions

Switch to [`control_flow.py`](control_flow.py), which runs as-is:

```bash
python3 control_flow.py
```

## Part D — Making decisions

### Exercise 7: Classify a star by its temperature

Astronomers sort stars into **spectral classes** by surface temperature. From
hottest to coolest these are **O, B, A, F, G, K, M** (our Sun is a G star).

Given a temperature in kelvin, print the spectral class using
`if` / `elif` / `else`. Use these approximate boundaries:

| Class | Temperature (K)      |
|:-----:|----------------------|
| O     | 30000 and above      |
| B     | 10000 – 30000        |
| A     | 7500 – 10000         |
| F     | 6000 – 7500          |
| G     | 5200 – 6000          |
| K     | 3700 – 5200          |
| M     | below 3700           |

```python
temperature = 5778   # the Sun
if temperature >= 30000:
    print("Class O")
elif temperature >= 10000:
    print("Class B")
# TODO: fill in A, F, G, K ...
else:
    print("Class M")
```

> The order matters: because each `elif` only runs when the ones above it were
> `False`, checking from hottest to coolest lets you use simple `>=` tests.

### Exercise 8: Boolean logic — can you see it?

A star is visible to the **naked eye** if its apparent magnitude is less than
about `6.0` (remember: smaller magnitude = brighter). Using `and` / `or` / `not`,
decide and print whether a star is *both* visible to the naked eye *and* bright
enough to see from a light-polluted city (say, magnitude less than `3.0`):

```python
magnitude = 1.25
naked_eye = magnitude < 6.0
city_visible = magnitude < 3.0
# TODO: print whether it is visible in the city (naked_eye AND city_visible)
```

---

## Part E — Repeating things

### Exercise 9: A `for` loop with `range()`

`range(1, 11)` gives you the numbers 1, 2, …, 10. Use a `for` loop to print a
small **light-travel table**: for each distance from 1 to 10 light-years, print
the year in which the light we see *now* (in 2026) left the star.

```python
for distance in range(1, 11):
    year_left = 2026 - distance
    print(f"{distance} ly  ->  light left in {year_left}")
```

Change `range(1, 11)` to `range(0, 21, 5)` and run it again — what does the
third number do?

### Exercise 10: A `while` loop

A `while` loop repeats **until a condition stops being true**. Start with a
brightness of `100` units and halve it each step, counting how many steps it
takes to drop below `1`:

```python
brightness = 100.0
steps = 0
while brightness >= 1.0:
    brightness = brightness / 2
    steps = steps + 1
# TODO: print how many steps it took
```

> **Careful:** make sure the value you test actually changes inside the loop,
> or it will run forever. If that happens, press **Ctrl + C** to stop it.

---

## Part F — Functions

### Exercise 11: Turn your classifier into a function

Refactor Exercise 7 into a **function** that takes a temperature and **returns**
the class letter (a string), instead of printing it:

```python
def spectral_class(temperature):
    if temperature >= 30000:
        return "O"
    elif temperature >= 10000:
        return "B"
    # TODO: A, F, G, K ...
    else:
        return "M"

print(spectral_class(5778))   # should print G
print(spectral_class(25000))  # should print B
```

Returning a value (instead of printing) is more useful, because now other code
can *use* the answer.

### Exercise 12: A function with a default argument

Write a function `light_left_year(distance_ly, now=2026)` that returns the year
the light left a star. The `now=2026` is a **default argument** — callers can
leave it out:

```python
def light_left_year(distance_ly, now=2026):
    return now - distance_ly

print(light_left_year(8.6))          # uses now = 2026
print(light_left_year(8.6, 2000))    # overrides now
```

### Optional extension for Week 2

Combine a loop *and* your function: loop over temperatures from `3000` to
`40000` in steps of `1000` and, for each one, print the temperature next to the
spectral class returned by `spectral_class(...)`. This is the same pattern —
"do something for every value in a range" — that NumPy will later let us do to
whole datasets at once.

---

## Submitting your work

**One submission, due by midnight on the day of the second session.**

1. Make sure **both** programs run without errors:
   ```bash
   python3 intro_to_python.py
   python3 control_flow.py
   ```
2. Add a short note (as comments, or in a new markdown file) about anything that
   surprised you coming from C++, or that tripped you up — indentation is a
   common one.
3. **Commit** and **push** your work:
   ```bash
   git add .
   git commit -m "Complete Lab V: Introduction to Python"
   git push
   ```
4. **Open a pull request** and let your instructor know you've finished.

Next lab we meet Python's built-in ways of holding *collections* of data —
lists, tuples and dictionaries — and then NumPy arrays, so we can stop writing
one variable per star.
