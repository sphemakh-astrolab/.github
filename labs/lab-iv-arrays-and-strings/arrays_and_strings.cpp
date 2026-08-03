// Lab IV: Arrays and Strings
// Programming Essentials for Astronomy I - C++
//
// This file is a skeleton. It gives you the STRUCTURE of the program - the
// order things go in, and what each piece is for - and nothing else. You write
// all of the code yourself. The README has worked examples of the syntax to
// get you going; turning them into the exercises is your job.
//
// Compile and run with:
//     g++ arrays_and_strings.cpp -o arrays_and_strings
//     ./arrays_and_strings
//
// Keep the exercise comments in place as you go, so your submission is easy to
// follow.

// TODO: include the three headers you need - <iostream>, <string>, and
// <cctype> (the last one is where std::toupper lives).


// ---------------------------------------------------------------------------
// Our star catalogue: three parallel arrays of length 8, so that index i
// describes the same star in all three - names, distance and magnitude.
// ---------------------------------------------------------------------------

// TODO: declare the three arrays. The eight stars and their values are in the
// README.


// --- Part A: functions over arrays -----------------------------------------

// Exercise 2: the average of the first n values of an array of doubles.
// TODO: write a function that adds the values up in a loop, then divides by n.

// Exercise 3: the INDEX of the smallest value in an array of doubles.
// TODO: write a function that assumes index 0 is smallest, then checks the rest.

// Exercise 3 (cont.): the INDEX of the largest value.
// TODO: write a function the same shape as the one above, looking for the
// largest value instead.


// --- Part B: functions over strings ----------------------------------------

// Exercise 7: a string with every letter capitalised.
// TODO: write a function that loops over each character and uses
// std::toupper(...) on it.


// ---------------------------------------------------------------------------
// Start the main function here
// ---------------------------------------------------------------------------

    // Exercise 1: print the catalogue using a for loop.
    // TODO: loop from 0 to N-1 and print index, name, distance and magnitude.

    // Exercise 2: print the average distance.
    // TODO: call your mean function on the distance array and print the result.

    // Exercise 3: print the nearest and the farthest star (by name).
    // TODO: use your two index functions on the distance array.

    // Exercise 4: print the brightest star (smallest magnitude).
    // TODO: use your smallest-index function on the magnitude array.

    // Exercise 5: measure and index one star name.
    // TODO: print a name's length, its first character and its last character.

    // Exercise 6: build and print a catalogue label for every star.
    // TODO: use string concatenation (+) and std::to_string(...).

    // Exercise 7: print every star's name in UPPERCASE.
    // TODO: call your capitalising function inside a loop.

    // Exercise 8 (challenge): check whether a designation starts with "HD".
    // TODO: test strings like "HD 48915", "HR 2491" and "HD 39801".
