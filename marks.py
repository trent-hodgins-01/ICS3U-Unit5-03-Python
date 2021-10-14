# !/user/bin/env python3

# Created by Trent Hodgins
# Created on 10/14/2021
# This is the Mark program
# The user enters in a mark level
# The program displays the level as a percentage


def calculate_percentage(level):
    # calculate percentage

    if level == "4+":
        percentage = 97
    elif level == "4":
        percentage = 90
    elif level == "4-":
        percentage = 83
    elif level == "3+":
        percentage = 78
    elif level == "3":
        percentage = 75
    elif level == "3-":
        percentage = 71
    elif level == "2+":
        percentage = 68
    elif level == "2":
        percentage = 65
    elif level == "2-":
        percentage = 61
    elif level == "1+":
        percentage = 58
    elif level == "1":
        percentage = 55
    elif level == "1-":
        percentage = 51
    elif level == "R":
        percentage = 0
    else:
        percentage = -1

    return percentage


def main():
    # this function gets the level

    # input
    level = input("Enter in grade mark(ex. 3-): ")
    print("")

    # call functions
    calculated_percentage = calculate_percentage(level)

    print("{0}%".format(calculated_percentage))
    print("\nDone.")


if __name__ == "__main__":
    main()
