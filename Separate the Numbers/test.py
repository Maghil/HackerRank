#!/bin/python3

import math
import os
import random
import re
import sys


def orderCheck(number: str, starting_digit_count: int) -> list(str,int,bool):
    """ returns(number, digit_count, final_iteration)"""
    print(f"{number = }")
    print(f"{starting_digit_count = }")
    print("\n")
    for digit_count in range(starting_digit_count, int(len(number)/2)+1):
        return_digit_count = digit_count
        first_number = int(number[:digit_count])
        if first_number % 10 == 9 and not (int(number[digit_count:digit_count+1]) % 10 == 9):
            second_number = int(number[digit_count:digit_count*2+1])
            return_digit_count = digit_count+1
        else:
            second_number = int(number[digit_count:digit_count*2])
        print(f"{digit_count = }")
        print(f"{first_number = }")
        print(f"{second_number = }")
        print("\n")
        if second_number - first_number == 1:
            if (len(number[digit_count:]) == return_digit_count):
                return(number[digit_count:], return_digit_count, True)
            else:
                return(number[digit_count:], return_digit_count, False)
    else:
        return(0, -1, False)


def separateNumbers(number:str):
    """starting number is to save the first number"""
    digit_count = 1
    starting_number = 0
    is_final_iteration = False
    temp_number = number
    while(digit_count > 0 and not is_final_iteration):
        temp_number, digit_count, is_final_iteration = orderCheck(
            temp_number, digit_count)
        #storing the starting number
        if starting_number == 0:
            starting_number = number[:digit_count]
        if digit_count < 0:
            print("NO")
            break
        elif digit_count > 0 and is_final_iteration:
            print(f"YES", starting_number)
            break


if __name__ == '__main__':
    numbers = [12345, 101112, 12310, 9101112,
               99100101102, 100101102, "010203", 99100, 99991000010001]
    numbers2=[1234567891011121314151617181920,5678910111213141516171819202122,9101112131415161718192021222324,979899100101102103104105106107,998999100010011002100310041005,1234567891011120314151617181920,5678910111213140516171819202122,9101112131415160718192021222324,979899100101102003104105106107,998999100010011902100310041005]
    separateNumbers(str(numbers[0]))
    # for i in numbers2:
    #     print("==================== {} ====================".format(i))
    #     separateNumbers(i)
