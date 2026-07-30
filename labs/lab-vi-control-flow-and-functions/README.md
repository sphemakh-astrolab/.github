# Lab VI: Control Flow and Functions in Python

**Programming Essentials for Astronomy I — Python**

In Lab III you taught C++ programs to **make decisions** (`if`/`else`), to
**repeat work** (loops), and to organise code into **functions**. This lab does
exactly the same things — in Python. You already know the ideas; here you'll see
how much cleaner they look.

The one genuinely new habit Python demands is **indentation**: instead of curly
braces `{ }`, Python uses the *spaces at the start of a line* to decide what is
"inside" an `if` or a loop or a function. Line up your code carefully and it
reads beautifully; get it wrong and Python will tell you.

---

## Learning goals

By the end of this lab you should be able to:

1. Make decisions with **`if` / `elif` / `else`**.
2. Combine conditions with the **comparison** (`==`, `!=`, `<`, `>=`, ...) and
   **boolean** (`and`, `or`, `not`) operators.
3. Repeat work with a **`for` loop** over `range(...)` and with a **`while`** loop.
4. Use **indentation** correctly to mark out blocks of code.
5. Define your own **functions** with `def`, including parameters, `return`
   values, and default arguments.

## Before you start

- Work in your Ubuntu (WSL) terminal with this repo open in **VSCode**.
- The starter file [`control_flow.py`](control_flow.py) runs as-is:
  ```bash
  python3 control_flow.py
  ```
- Remember: **no compiling** — edit the file, run it again.

---

## C++ vs Python reminders

| Idea            | C++                                        | Python                          |
|-----------------|--------------------------------------------|---------------------------------|
| If / else       | `if (x > 0) { ... } else { ... }`          | `if x > 0:` / `else:`           |
| "else if"       | `else if (...)`                            | `elif ...:`                     |
| For loop        | `for (int i = 0; i < 10; i++)`             | `for i in range(10):`           |
| While loop      | `while (x > 0) { ... }`                    | `while x > 0:`                  |
| Blocks          | curly braces `{ }`                         | **indentation** + a colon `:`   |
| Function        | `int f(int n) { return n; }`               | `def f(n):` / `return n`        |
| And / or / not  | `&&` / `\|\|` / `!`                        | `and` / `or` / `not`            |

Notice the pattern: a line that opens a block **ends in a colon `:`**, and
everything inside it is **indented** (4 spaces is standard).

---

## Part A — Making decisions

### Exercise 1: Classify a star by its temperature

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

### Exercise 2: Boolean logic — can you see it?

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

## Part B — Repeating things

### Exercise 3: A `for` loop with `range()`

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

### Exercise 4: A `while` loop

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

## Part C — Functions

### Exercise 5: Turn your classifier into a function

Refactor Exercise 1 into a **function** that takes a temperature and **returns**
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

### Exercise 6: A function with a default argument

Write a function `light_left_year(distance_ly, now=2026)` that returns the year
the light left a star. The `now=2026` is a **default argument** — callers can
leave it out:

```python
def light_left_year(distance_ly, now=2026):
    return now - distance_ly

print(light_left_year(8.6))          # uses now = 2026
print(light_left_year(8.6, 2000))    # overrides now
```

---

## Optional extension

Combine a loop *and* your function: loop over temperatures from `3000` to
`40000` in steps of `1000` and, for each one, print the temperature next to the
spectral class returned by `spectral_class(...)`. This is the same pattern —
"do something for every value in a range" — that NumPy will later let us do to
whole datasets at once.

---

## Submitting your work

1. Make sure your program **runs** without errors:
   ```bash
   python3 control_flow.py
   ```
2. Add a short note (as comments, or in a new markdown file) about anything that
   tripped you up — indentation is a common one.
3. **Commit** and **push**:
   ```bash
   git add .
   git commit -m "Complete Lab VI: Control Flow and Functions in Python"
   git push
   ```
4. **Open a pull request** and let your instructor know you've finished.

Next lab we meet Python's built-in ways of holding *collections* of data —
lists, tuples and dictionaries — so we can stop writing one variable per star.
