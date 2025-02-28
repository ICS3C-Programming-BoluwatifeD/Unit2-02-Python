#!/usr/bin/env python3
# Created By: Boluwatife Dada
# Date: feb 26, 2025
# This program asks the user for a radius of a circle mm. it then calculates and displays the circumference using tau
import constants

def main():
    # get the radius from the user
    radius = float(input("enter the radius of a circle(mm): "))
    # calculate the circumference
    circumference = constants.TAU * radius

    # display the circumference
    print("")
    print("circumference = {}mm".format(circumference))


if __name__ == "__main__":
    main()
