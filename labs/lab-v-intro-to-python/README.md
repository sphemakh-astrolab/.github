# Lab V: A Gentle Introduction to Python

**Programming Essentials for Astronomy I — Python**

Welcome to Python! For the rest of the course we switch from C++ to
[Python](https://www.python.org), the language we'll use to do real scientific
data analysis. The good news: everything you learned in C++ — variables, types,
arithmetic, input and output — still applies. Python just lets you express it
with a lot less ceremony.

This first lab is deliberately gentle. We'll take a few calculations you already
know how to do in C++ and re-do them in Python, so you can *feel* the
differences. Later labs build on this towards data structures, files, and the
NumPy and Matplotlib libraries for scientific computing.

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
6. Re-implement a small C++ calculation in Python and compare the two.

## Before you start

- Work in your Ubuntu (WSL) terminal, with this repository open in **VSCode**.
- Check Python is installed:
  ```bash
  python3 --version
  ```
- A starter file, [`intro_to_python.py`](intro_to_python.py), is provided with
  `TODO`s to fill in. It already runs — try it now:
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
| Blocks               | `{ curly braces }`                   | **indentation** (spaces)      |
| Power (e.g. r³)      | `r * r * r` (no built-in operator)   | `r ** 3`                      |

---

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

---

## Optional extension

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

## Submitting your work

1. Make sure your program **runs** without errors:
   ```bash
   python3 intro_to_python.py
   ```
2. Add a short note (as comments, or in a new markdown file) about anything that
   surprised you coming from C++.
3. **Commit** and **push** your work:
   ```bash
   git add .
   git commit -m "Complete Lab V: A Gentle Introduction to Python"
   git push
   ```
4. **Open a pull request** and let your instructor know you've finished.

Next lab we bring back **loops, conditionals and functions** — this time in
Python.
