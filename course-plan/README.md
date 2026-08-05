# Course Plan — Semester 2

**Programming Essentials for Astronomy I: C++ and Python**

This semester we finish off the **C++** section with arrays and strings, then
move to **Python**, which we use to learn the fundamentals of **scientific data
analysis**. Labs continue from where we left off in Semester 1 (which ended at
Lab III), so this semester runs **Lab IV → Lab IX**.

Each lab is a GitHub Classroom exercise with an astronomy theme. Every lab has
its **own repository** in the
[sphemakh-astrolab](https://github.com/orgs/sphemakh-astrolab/repositories)
organisation, which is where its instructions and starter files live.

> **A lab's repository opens on the day of that lab.** Until then the link below
> will give you a "404 — not found" page. That is expected, not a broken link:
> the repository exists, it just isn't public yet.

---

## How the labs work

- **Each lab runs over two sessions.** In week 1 a short mini-lecture introduces
  the new material and you start the exercise; in week 2 you carry on and
  **submit by midnight that same day**.
- Lab IV is the one exception: it carries over from Block 2 and gets a single
  session.
- **Lab IX, the capstone, is split across the semester.** Its two sessions are
  not consecutive: you collect the data at the Digital Dome on **17 August** and
  do the modelling and write-up on **26 October**. The Dome chose the date, which
  is why the capstone appears before Lab V in the schedule below.
- Every lab has a starter file laying out the structure and the exercises, so you
  never face a blank page. How much code it hands you varies: some labs give you
  a running program to extend, others give you the skeleton and worked examples
  in the lab README, and you write the code.
- You submit by committing and pushing your work and opening a pull request, then
  letting your instructor know (same workflow as Semester 1).

---

## Schedule

> ### ⚠ The Digital Dome visit is on **Monday 17 August**
>
> The Dome has given us **17 August** for the Lab IX capstone visit, so the
> capstone's data-collection session happens *early* — out of numerical order,
> before Lab V. Every other lab shifts one Monday later to make room. Dates below
> may still shift around the spring recess, so **check this page before each
> session** — it is always the up-to-date version.

### Block 3 · 27 July – 4 September · *Finishing C++ & Launching Python*

| Date          | Lab                                                                       | Session                                        |
|---------------|---------------------------------------------------------------------------|------------------------------------------------|
| 03 August     | [**Lab IV** — Arrays and Strings *(C++)*](https://github.com/sphemakh-astrolab/lab-iv-arrays-and-strings)                                   | Single session — carried over; submit by Fri 7 Aug, 23:59  |
| ~~10 August~~ | *No lab — Women's Day (observed Monday, as 9 August is a Sunday)*         | —                                              |
| **17 August** | [**Lab IX** — Capstone Project: Predicting a Planetary Alignment](https://github.com/sphemakh-astrolab/lab-ix-capstone-planetary-alignment) | **Digital Dome — data collection. Be seated by 14:00; we start at 14:15.** |
| 24 August     | [**Lab V** — Introduction to Python: Basics, Control Flow and Functions](https://github.com/sphemakh-astrolab/lab-v-python-basics-and-control-flow)    | Week 1 — mini-lecture, start the lab           |
| 31 August     | **Lab V** — continued                                                     | Week 2 — submit by midnight                    |

### Block 4 · 14 September – 27 October · *Scientific Computing & Data Analysis*

| Date         | Lab                                                                                                                     | Session                                     |
|--------------|-------------------------------------------------------------------------------------------------------------------------|---------------------------------------------|
| 14 September | **Lab VI** — Python Data Structures and NumPy Arrays                                                                    | Week 1 — mini-lecture, start the lab        |
| 21 September | **Lab VI** — continued                                                                                                  | Week 2 — submit by midnight                 |
| 28 September | **Lab VII** — Data File I/O and Plotting with Matplotlib                                                                | Week 1 — mini-lecture, start the lab        |
| 05 October   | **Lab VII** — continued                                                                                                 | Week 2 — submit by midnight                 |
| 12 October   | **Lab VIII** — Analysing Tabular Data                                                                                   | Week 1 — mini-lecture, start the lab        |
| 19 October   | **Lab VIII** — continued                                                                                                | Week 2 — submit by midnight                 |
| 26 October   | **Lab IX** — continued                                                                                                  | Week 2 — computer lab; submit by midnight   |

> ### About the Dome visit on 17 August
>
> - **Be at the Dome by 14:00.** We start at 14:15 sharp — the Dome steps through
>   the twelve epochs once, for the whole room, and there is no way to replay them
>   for latecomers.
> - **You need no Python at all for this session.** You are there to *measure*:
>   read positions off the screen and write them down. The programming comes later.
> - **Work alone or in pairs**, and record all twelve epochs yourself. Do not
>   split the epochs between you — a full set measured by one person is more
>   consistent than a set stitched together from several.
> - **Guard your data.** You will not use it until **26 October**, ten weeks
>   later. Commit it to your capstone repository the same week; a lost data file
>   cannot be re-measured.

> Note that **the capstone spans the whole semester** — you collect the data on
> 17 August and do the modelling and write-up on 26 October, once you have the
> Python, NumPy and plotting you need to handle it.

> Dates are Mondays within each block and may shift slightly around the spring
> recess and any public holidays — check here for the current version.

---



## What each lab covers

| Lab  | Title                                                          | You will learn                                                                                 |
|------|----------------------------------------------------------------|------------------------------------------------------------------------------------------------|
| IV   | [Arrays and Strings *(C++)*](https://github.com/sphemakh-astrolab/lab-iv-arrays-and-strings)                                     | Fixed-size arrays, looping over them, arrays as function arguments; `std::string` basics.       |
| V    | [Introduction to Python: Basics, Control Flow and Functions](https://github.com/sphemakh-astrolab/lab-v-python-basics-and-control-flow)     | Running Python, dynamic typing vs C++, variables, `print`/`input`, f-strings; `if/elif/else`, `for`/`while`, `range`, defining functions, importing modules. |
| VI   | Python Data Structures and NumPy Arrays                        | Lists, tuples, dictionaries, slicing, list comprehensions, string methods; `ndarray`, vectorised maths, indexing and boolean masking. |
| VII  | Data File I/O and Plotting with Matplotlib                     | Opening files, looping over lines, parsing a CSV of astronomical data; scatter/line plots, labels, log axes, saving figures. |
| VIII | Analysing Tabular Data                                         | Loading a real dataset, filtering, computing derived quantities, plotting a result (NumPy).     |
| IX   | [Capstone Project](https://github.com/sphemakh-astrolab/lab-ix-capstone-planetary-alignment) | Measure planetary positions in the Digital Dome → fit orbits → predict the date of the next Earth–Venus–Mars alignment → verify it, and write it up. |

The Python half deliberately re-does some early C++ tasks in Python first, so the
language switch feels natural, before opening up what Python makes easy:
data structures, file handling, vectorised NumPy, and plotting.
