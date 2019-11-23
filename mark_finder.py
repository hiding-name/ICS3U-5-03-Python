#!/usr/bin/env python3

# Created by: Matsuru Hoshi
# Created on: Nov 2019
# This is program mark finder


def mark_finder(level):
    # This'll determine the mark

    # This dictionnary keeps track of the levels associated with the marks
    marks = {
        "4+": "97.5",
        "4": "90.5",
        "4-": "83",
        "3+": "78",
        "3": "74.5",
        "3-": "71",
        "2+": "68",
        "2": "64.5",
        "2-": "61",
        "1+": "58",
        "1": "54.5",
        "1-": "51",
        "0+": "44.5",
        "0": "34.5",
        "0-": "14.5"
    }

    if level in marks:
        return(marks[level])
    else:
        return False
    # process


def main():
    # This is asks for the user input and runs mark_finder()

    # Welcomes user
    print("Hi, this is MARK FINDER.")
    print("Ex. level = 4+ >>> Your mark is 97.5%")
    input("Press Enter to continue.\n")

    while True:
        level = input("What is the level: ")
        # runs mark_finder()
        mark = mark_finder(level)
        if mark is False:
            print("\nSorry, you mark could not be determined.")
            print("Try again.\n")
        else:
            print("\nYour mark is " + mark + "%")
            break


if __name__ == "__main__":
    main()
