#!/usr/bin/env python3

# Created by: Haokai Li
# Created on: Sept 2021
# This Program check that twelve months


def main():
    # This function check that twelve months

    # input
    integer = int(input("Enter the number of month(ex: 3 for March): "))
    print("")

    # process
    if integer == 1:
        # output
        print("January")
    elif integer == 2:
        # output
        print("February")
    elif integer == 3:
        # output
        print("March")
    elif integer == 4:
        # output
        print("April")
    elif integer == 5:
        # output
        print("May")
    elif integer == 6:
        # output
        print("June")
    elif integer == 7:
        # output
        print("July")
    elif integer == 8:
        # output
        print("August")
    elif integer == 9:
        # output
        print("September")
    elif integer == 10:
        # output
        print("October")
    elif integer == 11:
        # output
        print("November")
    elif integer == 12:
        # output
        print("December")
    else:
        # output
        print("Pleace enter a number from 1 to 12")

    print("\nDone")


if __name__ == "__main__":
    main()
