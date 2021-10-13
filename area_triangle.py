#!/usr/bin/env python3

# Created by: Michael Zagon
# Created on: Oct 2021
# This program calculates the area of a triangle


def area(base, height):
    # This function calculates the area of a triangle

    # Process
    area = base * height / 2

    # Output
    print("\nThe area of the triangle is {0} cm².".format(area))


def main():
    # This function gets user inputs and calls functions

    # Input
    base_from_user = input("Enter the base length of the triangle (cm): ")
    height_from_user = input("Enter the base length of the triangle (cm): ")
    try:
        base_from_user = int(base_from_user)
        height_from_user = int(height_from_user)
        print("\nDone.")
        # Call functions
        area(base_from_user, height_from_user)
    except Exception:
        print("\nInvalid Input.")


if __name__ == "__main__":
    main()
