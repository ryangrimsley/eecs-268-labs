'''
Author: Ryan Grimsley
KUID: 3095998
Date: 2/20
Lab: lab4
Last modified: 2/20
Purpose: takes in a mode and integer and recursively either checks if that 
number is a fibonacci number or the ith fibonacci number based on the mode
'''
def ith_mode(i):
    if i == 0:
        return 0
    elif i ==1:
        return 1
    else:
        return ith_mode(i-1)+ith_mode(i-2)

def vth_mode(i):
    if i == 0:
        return True
    elif i == 1:
        return True
    elif i == 2:
        return True
    else:
        for j in range(2,i):
            if ith_mode(j-1)+ith_mode(j-2) == i:
                return True
            
        return False


def main():
    mode_and_value = input("Enter mode and value: ")
    mode_and_value_list = mode_and_value.strip().split()
    try:
        if int(mode_and_value_list[1]) >= 0:

            if mode_and_value_list[0] == '-i':
                print(ith_mode(int(mode_and_value_list[1])))

            elif mode_and_value_list[0] == '-v':
                if vth_mode(int(mode_and_value_list[1])):
                    print(f"{int(mode_and_value_list[1])} is in the sequence")
                else:
                    print(f"{int(mode_and_value_list[1])} is not in the sequence")
            else:
                print("Invalid mode")
        else:
            raise RuntimeError
    except:
        print("Invalid int")
        

if __name__ == "__main__":
    main()

