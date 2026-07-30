# Course Plan — Semester 2

**Programming Essentials for Astronomy I: C++ and Python**

This semester we finish off the **C++** section with arrays and strings, then
move to **Python**, which we use to learn the fundamentals of **scientific data
analysis**. Labs continue from where we left off in Semester 1 (which ended at
Lab III), so this semester runs **Lab IV → Lab XII**.

Each lab is a GitHub Classroom exercise with an astronomy theme. Lab materials
are kept in this repository under [`labs/`](../labs).

---

## How the labs work

- One lab per session, building on the previous one.
- Every lab has a starter with clear exercises — you always start from working,
  compilable code, not a blank page.
- You submit by committing and pushing your work and opening a pull request, then
  letting your instructor know (same workflow as Semester 1).

---

## Schedule

### Block 3 · 27 July – 4 September · *Finishing C++ & Launching Python*

| Date       | Lab                                                    |
|------------|--------------------------------------------------------|
| 03 August    | **Lab IV** — Arrays and Strings *(C++)*              |         |
| ~~10 August~~ | *No lab — Women's Day (public holiday)*             |
| 17 August  | **Lab VI** — Basic Python + Control Flow and Functions |
| 24 August  | **Lab VII** — Python Data Structures                   |
| 31 August  | **Lab VIII** — Reading and Writing Data Files          |

### Block 4 · 14 September – 27 October · *Scientific Computing & Data Analysis*

| Date         | Lab                                                  |
|--------------|------------------------------------------------------|
| 14 September | **Lab IX** — NumPy Arrays +                          |
| 21 September | **Lab X** — Plotting with Matplotlib                 |
| 05 October   | **Lab XI** — Analysing Tabular Data                  |
| 19 October   | **Lab XII** — Capstone Mini-Project                  |

> Dates are Mondays within each block and may shift slightly around the spring
> recess and any public holidays — check here for the current version.

---



## What each lab covers

| Lab  | Title                              | You will learn                                                                                 |
|------|------------------------------------|------------------------------------------------------------------------------------------------|
| IV   | Arrays and Strings *(C++)*         | Fixed-size arrays, looping over them, arrays as function arguments; `std::string` basics.       |
| V(a) | A Gentle Introduction to Python    | Running Python, dynamic typing vs C++, variables, `print`/`input`, f-strings.                   |
| V(b) | Control Flow and Functions         | `if/elif/else`, `for`/`while`, `range`, defining functions, importing modules.                  |
| VI   | Python Data Structures             | Lists, tuples, dictionaries, slicing, list comprehensions, string methods.                      |
| VII  | Reading and Writing Data Files     | Opening files, looping over lines, parsing a CSV of astronomical data.                          |
| VIII | NumPy Arrays                       | `ndarray`, vectorised maths, indexing and boolean masking.                                      |
| IX   | Plotting with Matplotlib           | Scatter/line plots, labels, log axes, saving figures.                                           |
| X    | Analysing Tabular Data             | Loading a real dataset, filtering, computing derived quantities, plotting a result (NumPy).     |
| XI   | Capstone Mini-Project              | Read real astronomical data → analyse → produce a labelled plot → push and open a pull request. |

The Python half deliberately re-does some early C++ tasks in Python first, so the
language switch feels natural, before opening up what Python makes easy:
data structures, file handling, vectorised NumPy, and plotting.
