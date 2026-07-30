// Lab IV: Arrays and Strings
// Programming Essentials for Astronomy I - C++
//
// Fill in the TODOs below. Compile and run with:
//     g++ arrays_and_strings.cpp -o arrays_and_strings
//     ./arrays_and_strings

#include <iostream>
#include <string>
#include <cctype>   // for std::toupper

// ---------------------------------------------------------------------------
// Our star catalogue (parallel arrays: index i describes the same star in all
// three arrays).
// ---------------------------------------------------------------------------
const int N = 8;

std::string names[N] = {"Sirius", "Canopus", "Alpha Centauri", "Arcturus",
                        "Vega", "Rigel", "Procyon", "Betelgeuse"};
double distance[N]   = {8.6, 310.0, 4.4, 37.0, 25.0, 860.0, 11.5, 640.0};
double magnitude[N]  = {-1.46, -0.74, -0.27, -0.05, 0.03, 0.13, 0.34, 0.42};


// --- Part A: functions over arrays -----------------------------------------

// Exercise 2: return the average of the first n values in data.
double mean(const double data[], int n) {
    // TODO: add the values up in a loop and divide by n.
    return 0.0;  // replace this
}

// Exercise 3: return the INDEX of the smallest value in data.
int indexOfMin(const double data[], int n) {
    // TODO: start by assuming index 0 is smallest, then check the rest.
    return 0;  // replace this
}

// Exercise 3 (cont.): return the INDEX of the largest value in data.
int indexOfMax(const double data[], int n) {
    // TODO: like indexOfMin, but looking for the largest value.
    return 0;  // replace this
}


// --- Part B: functions over strings ----------------------------------------

// Exercise 7: return text with every letter capitalised.
std::string toUpper(std::string text) {
    // TODO: loop over each character and use std::toupper(...)
    return text;  // replace this
}


int main() {
    // Exercise 1: print the catalogue using a for loop.
    std::cout << "--- Star catalogue ---" << std::endl;
    // TODO: loop from 0 to N-1 and print index, name, distance and magnitude.

    // Exercise 2: print the average distance.
    // TODO: call mean(distance, N) and print the result.

    // Exercise 3: print the nearest and the farthest star (by name).
    // TODO: use indexOfMin / indexOfMax on the distance array.

    // Exercise 4: print the brightest star (smallest magnitude).
    // TODO: use indexOfMin on the magnitude array.

    // Exercise 5: measure and index one star name.
    // TODO: print a name's length, first character and last character.

    // Exercise 6: build and print a catalogue label for every star.
    // TODO: use string concatenation (+) and std::to_string(...).

    // Exercise 7: print every star's name in UPPERCASE.
    // TODO: call your toUpper(...) function inside a loop.

    // Exercise 8 (challenge): check whether a designation starts with "HD".
    // TODO: test strings like "HD 48915", "HR 2491", "HD 39801".

    return 0;
}
