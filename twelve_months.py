#!/usr/bin/env python3

# Created by: Haokai Li
# Created on: Sept 2021
# This Program check that twelve months


def main():
    # This function check that twelve months

    # input
    month_number = int(input("Enter the number of months(ex: 3 for March): "))
    print("")

    # process
    if month_number == 1:
        # output
        print("January")
    elif month_number == 2:
        # output
        print("February")
    elif month_number == 3:
        # output
        print("March")
    elif month_number == 4:
        # output
        print("April")
    elif month_number == 5:
        # output
        print("May")
    elif month_number == 6:
        # output
        print("June")
    elif month_number == 7:
        # output
        print("July")
    elif month_number == 8:
        # output
        print("August")
    elif month_number == 9:
        # output
        print("September")
    elif month_number == 10:
        # output
        print("October")
    elif month_number == 11:
        # output
        print("November")
    elif month_number == 12:
        # output
        print("December")
    else:
        # output
        print("Pleace enter a number from 1 to 12")

    print("\nDone")


if __name__ == "__main__":
    main()
