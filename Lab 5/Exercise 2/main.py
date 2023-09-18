'''
Author: Ryan Grimsley
KUID: 3095998
Date: 2/20
Lab: lab4
Last modified: 2/20
Purpose: takes in a day and recursively gives back how many people have the flu at that time
'''


def calculate_sick_count(day):
    if day == 1:
        return 6
    elif day == 2:
        return 20
    elif day == 3:
        return 75
    else:
        sick = calculate_sick_count(day-1)+calculate_sick_count(day-2)+calculate_sick_count(day-3)
        return sick

def main():
    day = int(input("What day do you want the sick count for?: "))
    if day <= 0:
        print("Invalid day")
    else:
        print(calculate_sick_count(day))


if __name__ == "__main__":
    main()