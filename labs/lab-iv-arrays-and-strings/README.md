# Lab IV: Arrays and Strings

**Programming Essentials for Astronomy I — C++**

In Lab II you met C++ (variables, types, input/output) and in Lab III you learned to control the flow of a program with **functions**,
**loops** and **conditionals**. In the Kepler lab you even looped over a table of planets and wrote your own function to find the smallest value in a list.

This lab is the last stop on our C++ tour. We will make that idea of a "list of values" official by learning **arrays**, and we will learn how the computer stores text using **strings**. Together, arrays and strings are how we start to handle *real* astronomical data — a catalogue of stars, each with a name and a set of measurements.

By the end of this lab you should be comfortable answering questions like *"which of these stars is the closest?"* and *"what is the average distance to the brightest stars?"* — using code you wrote yourself.

---

## Learning goals

By the end of this lab you should be able to:

1. Declare and initialise a **fixed-size array**, and access its elements by index.
2. Understand **zero-based indexing** and why reading past the end of an array is dangerous.
3. **Loop over an array** to print it and to compute totals, averages, minimums and maximums.
4. **Pass an array to a function** (together with its size).
5. Use the **`std::string`** type: measure its length, read individual characters, join strings together, and compare them.
6. Combine arrays and strings to work with a small **star catalogue**.

## Before you start

- Make sure you can already compile and run a C++ program from the terminal
  (see Lab II and the [course Wiki](https://github.com/sphemakh-astrolab/.github/wiki)).
- Open this repository in **VSCode** and work inside your Ubuntu (WSL) terminal.
- A starter file, [`arrays_and_strings.cpp`](arrays_and_strings.cpp), lays out the
  **structure** of the program as `TODO` comments. You write all of the code, but
  you don't have to work out the shape of it from scratch — and the examples below
  show you the syntax you'll need.

To compile and run your program:

```bash
g++ arrays_and_strings.cpp -o arrays_and_strings
./arrays_and_strings
```

Recompile every time you change the code — the computer does not run your `.cpp` file directly, it runs the program you build from it.

---

## Our dataset: the brightest stars in the night sky

Throughout this lab we will use the eight brightest stars visible from Earth. For each star we have its **name**, its **distance** from us in light-years (ly), and its **apparent magnitude** (how bright it *looks* from Earth — remember that **smaller magnitude means brighter**, and it can be negative!).

| Index | Star            | Distance (ly) | Apparent magnitude |
|:-----:|-----------------|--------------:|-------------------:|
| 0     | Sirius          |           8.6 |              -1.46 |
| 1     | Canopus         |         310.0 |              -0.74 |
| 2     | Alpha Centauri  |           4.4 |              -0.27 |
| 3     | Arcturus        |          37.0 |              -0.05 |
| 4     | Vega            |          25.0 |               0.03 |
| 5     | Rigel           |         860.0 |               0.13 |
| 6     | Procyon         |          11.5 |               0.34 |
| 7     | Betelgeuse      |         640.0 |               0.42 |

We will store this table in your program as **three parallel arrays**: one for the names, one for the distances, and one for the magnitudes. "Parallel" means that everything at index `i` belongs to the same star — `names[2]`, `distance[2]` and `magnitude[2]` all describe Alpha Centauri.

```cpp
#include <string>

std::string names[8]   = {"Sirius", "Canopus", "Alpha Centauri", "Arcturus",
                          "Vega", "Rigel", "Procyon", "Betelgeuse"};
double distance[8]     = {8.6, 310.0, 4.4, 37.0, 25.0, 860.0, 11.5, 640.0};
double magnitude[8]    = {-1.46, -0.74, -0.27, -0.05, 0.03, 0.13, 0.34, 0.42};
```

---

## Part A — Arrays

### Exercise 1: Print the catalogue

Using a **`for` loop**, print each star as a neat row, for example:

```
0  Sirius           8.6 ly    mag -1.46
1  Canopus          310 ly    mag -0.74
...
```

Don't worry about lining the columns up exactly — a space or a tab between the
values is fine. Neat column alignment needs output formatting we haven't met yet.

> **Hint:** the array has 8 elements, so your loop index should run from `0` up
> to (but not including) `8`. The valid indices are `0,1,2,...,7` — there is no
> element at index `8`.

### Exercise 2: The average distance

Write a **function**

```cpp
double mean(const double data[], int n);
```

that returns the average of the first `n` values in `data`. Do **not** use any
built-in maths library for this — add the values up in a loop and divide by
`n`, exactly as you would by hand. Use it to print the **average distance** to
these eight stars.

> Notice that arrays don't remember their own size, so we must pass the number
> of elements (`n`) as a second argument. The `const` promises the function will
> not modify the array.

### Exercise 3: The nearest and farthest star

Write a function

```cpp
int indexOfMin(const double data[], int n);
```

that returns the **index** of the smallest value (this is the same idea you used
in the Kepler lab). Use it on the `distance` array to find the nearest star, and
**print its name** — this is where parallel arrays shine: the index you get back
also tells you where the name lives.

Then write (or adapt) an `indexOfMax` function and use it to print the
**farthest** star.

### Exercise 4: The brightest star

Remember that **brighter stars have smaller magnitudes**. Reuse your
`indexOfMin` function — this time on the `magnitude` array — to find and print
the **brightest** star in our catalogue. (Does the answer match what you know
about the night sky?)

---

## Part B — Strings

A `std::string` is C++'s way of storing text. You can think of it as an array of
characters, and many of the array ideas above carry straight over.

```cpp
#include <string>
std::string name = "Sirius";
```

### Exercise 5: Measuring and indexing text

A string knows its own length, and you can pull out a single character by index
just like an array. For example:

```cpp
std::string constellation = "Orion";
std::cout << constellation.length() << std::endl;  // how many characters
std::cout << constellation[0] << std::endl;        // the character at index 0
```

Pick one star name from the catalogue and print how many characters it has, its
**first** character, and its **last** character.

> **Hint:** just like the star arrays, strings are zero-indexed. The last valid
> character is at index `length - 1`, not `length` — work out what to put in the
> square brackets.

### Exercise 6: Building a catalogue label

We often want to build a single line of text out of several pieces. Strings can
be **joined together with `+`** (this is called *concatenation*). To glue a
number onto a string, first turn it into text with `std::to_string(...)`:

For example, joining a name and a number into one piece of text:

```cpp
std::string planet = "Mars";
double au = 1.52;
std::string line = planet + " orbits at " + std::to_string(au) + " AU";
```

Write a loop that prints a one-line **catalogue label** for **every** star,
looking something like:

```
[Sirius] distance = 8.600000 ly
[Canopus] distance = 310.000000 ly
...
```

> **That is not a mistake:** `std::to_string(...)` always writes a `double` with
> six decimal places, so `8.6` comes out as `8.600000`. Your program is working
> correctly — leave it as it is. Tidying it up needs output formatting, which we
> meet later.

### Exercise 7: SHOUTING the names

Write a function

```cpp
std::string toUpper(std::string text);
```

that returns the text with every letter turned into a **capital** letter. Loop over the characters and use `std::toupper(...)` from the `<cctype>` header on
each one. Print each star's name in uppercase, e.g. `SIRIUS`, `CANOPUS`, ...

A string can be **written to** by index, not just read from — so you can change a
character in place:

```cpp
std::string word = "orion";
word[0] = std::toupper(word[0]);   // word is now "Orion"
```

That does one character; the exercise asks for all of them.

### Exercise 8 (challenge): Catalogue designations

Astronomers often refer to stars by a catalogue designation rather than a common name — for example, Sirius is also **"HD 48915"** in the Henry Draper catalogue.

Given a designation string, write code (or a function returning `bool`) that checks whether it **starts with `"HD"`**. Test it on a few strings such as
`"HD 48915"`, `"HR 2491"` and `"HD 39801"`.

> **Hint:** `designation.substr(0, 2)` gives you the first two characters as a
> new string, which you can then compare with `"HD"` using `==`.

---

## Optional extension

Combine everything: find the **nearest star whose name is longer than 6 characters**, and print a nicely formatted label for it. This mixes an array
search (Part A) with string length (Part B) — exactly the kind of small data question the rest of the course is built on.

---

## Submitting your work

1. Make sure your program **compiles and runs** without errors. 
2. Add a short note (in the code as comments, or in a new markdown file) about anything you found tricky or are still unsure about.
3. **Commit** your changes with a clear message, then **push** them:
   ```bash
   git add .
   git commit -m "Complete Lab IV: Arrays and Strings"
   git push
   ```
4. **Open a pull request** and let your instructor know you've finished the lab.

END of LAB
