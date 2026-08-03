# Course Plan — Semester 2

**Programming Essentials for Astronomy I: C++ and Python**

This semester we finish off the **C++** section with arrays and strings, then
move to **Python**, which we use to learn the fundamentals of **scientific data
analysis**. Labs continue from where we left off in Semester 1 (which ended at
Lab III), so this semester runs **Lab IV → Lab IX**.

Each lab is a GitHub Classroom exercise with an astronomy theme. Lab materials
are kept in this repository under [`labs/`](../labs).

---

## How the labs work

- **Each lab runs over two sessions.** In week 1 a short mini-lecture introduces
  the new material and you start the exercise; in week 2 you carry on and
  **submit by midnight that same day**.
- Lab IV is the one exception: it carries over from Block 2 and gets a single
  session.
- Every lab has a starter with clear exercises — you always start from working,
  compilable code, not a blank page.
- You submit by committing and pushing your work and opening a pull request, then
  letting your instructor know (same workflow as Semester 1).

---

## Schedule

### Block 3 · 27 July – 4 September · *Finishing C++ & Launching Python*

| Date          | Lab                                                                       | Session                                        |
|---------------|---------------------------------------------------------------------------|------------------------------------------------|
| 03 August     | **Lab IV** — Arrays and Strings *(C++)*                                   | Single session — carried over; submit tonight  |
| ~~10 August~~ | *No lab — Women's Day (observed Monday, as 9 August is a Sunday)*         | —                                              |
| 17 August     | **Lab V** — Introduction to Python: Basics, Control Flow and Functions    | Week 1 — mini-lecture, start the lab           |
| 24 August     | **Lab V** — continued                                                     | Week 2 — submit by midnight                    |
| 31 August     | **Lab VI** — Python Data Structures and NumPy Arrays                      | Week 1 — mini-lecture, start the lab           |

### Block 4 · 14 September – 27 October · *Scientific Computing & Data Analysis*

| Date         | Lab                                                                                                                     | Session                                     |
|--------------|-------------------------------------------------------------------------------------------------------------------------|---------------------------------------------|
| 14 September | **Lab VI** — continued                                                                                                  | Week 2 — submit by midnight                 |
| 21 September | **Lab VII** — Data File I/O and Plotting with Matplotlib                                                                | Week 1 — mini-lecture, start the lab        |
| 28 September | **Lab VII** — continued                                                                                                 | Week 2 — submit by midnight                 |
| 05 October   | **Lab VIII** — Analysing Tabular Data                                                                                   | Week 1 — mini-lecture, start the lab        |
| 12 October   | **Lab VIII** — continued                                                                                                | Week 2 — submit by midnight                 |
| 19 October   | [**Lab IX** — Capstone Project: Predicting a Planetary Alignment](../labs/lab-ix-capstone-planetary-alignment)          | Week 1 — Digital Dome visit                 |
| 26 October   | **Lab IX** — continued                                                                                                  | Week 2 — computer lab; submit by midnight   |

> Note that **Lab VI spans the break between the two blocks** — you start it on
> 31 August and submit it on 14 September. Use the gap; don't leave it all to the
> second session.

> Dates are Mondays within each block and may shift slightly around the spring
> recess and any public holidays — check here for the current version.

---



## What each lab covers

| Lab  | Title                                                          | You will learn                                                                                 |
|------|----------------------------------------------------------------|------------------------------------------------------------------------------------------------|
| IV   | Arrays and Strings *(C++)*                                     | Fixed-size arrays, looping over them, arrays as function arguments; `std::string` basics.       |
| V    | Introduction to Python: Basics, Control Flow and Functions     | Running Python, dynamic typing vs C++, variables, `print`/`input`, f-strings; `if/elif/else`, `for`/`while`, `range`, defining functions, importing modules. |
| VI   | Python Data Structures and NumPy Arrays                        | Lists, tuples, dictionaries, slicing, list comprehensions, string methods; `ndarray`, vectorised maths, indexing and boolean masking. |
| VII  | Data File I/O and Plotting with Matplotlib                     | Opening files, looping over lines, parsing a CSV of astronomical data; scatter/line plots, labels, log axes, saving figures. |
| VIII | Analysing Tabular Data                                         | Loading a real dataset, filtering, computing derived quantities, plotting a result (NumPy).     |
| IX   | [Capstone Project](../labs/lab-ix-capstone-planetary-alignment) | Measure planetary positions in the Digital Dome → fit orbits → predict the date of the next Earth–Venus–Mars alignment → verify it, and write it up. |

The Python half deliberately re-does some early C++ tasks in Python first, so the
language switch feels natural, before opening up what Python makes easy:
data structures, file handling, vectorised NumPy, and plotting.
