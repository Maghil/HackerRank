#!/bin/python3

import math
import os
import random
import re
import sys

def separateNumbers(number):
    temp_number = number_string=str(number)
    print(number)
    for position in range(1,int(len(str(number))/2+1)):
        first_number = number_string[:position]
        second_number = number_string[position:position*2]
        second_number_plus_one = number_string[position:position*2+1]
        if int(second_number) - int(first_number) == 1 or int(second_number_plus_one) - int(first_number) == 1:
            return True, number_string[position:]
    else:
        return False,0


if __name__ == '__main__':
    number0=12345
    number1=101112
    number3=12310
    number4=91011
    flag=True
    number=number0
    while(flag and len(str(number))>0):
        flag,number=separateNumbers(number)
        number=int(number)
    if flag==False:
        print("NO")
    else:
        print("YES ")

#divide extracts first part
# 12345/100 = 123