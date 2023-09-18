'''
Author: Ryan Grimsley
KUID: 3095998
Date: 2/20
Lab: lab4
Last modified: 2/20
Purpose: takes in a base and exponent and recursively gives back an answer
'''
def rec_exp(base, power):
    if power == 0:
        return 1
    elif power == 1:
        return base
    else:
        return base*rec_exp(base, power-1)
        
    

def main():
    isValid = False
    while not isValid:
        try:
            base = int(input("Enter a base: "))
            power = int(input("Enter a power: "))
            isValid = True
        except:
            print("Power and base must be integers")

    if power < 0:
        print("Sorry, your exponent must be zero or larger")

    else:
        print(rec_exp(base, power))


if __name__ == "__main__":
    main()


def exp(base, power):
    if power == 0:
        return 1
    elif power == 1:
        return base
    else:
        return exp(base, power-1)*base
print(exp(2,3))