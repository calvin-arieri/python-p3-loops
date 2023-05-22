#!/usr/bin/env python3

def happy_new_year():
    # code goes here!
    num = 11
    while num >= 1:
        num -= 1
        if num != 0:
            print(num)
        else:
            print("Happy New Year!")

def square_integers(int_list):
    # code goes here!
    squared_integers = list()
    for integer in int_list:
        squared_integers.append(integer**2)
    return squared_integers    


def fizzbuzz():
    # code goes here!
    num = 0
    while num < 100:
        num += 1
        if num % 3 == 0 and num % 5 != 0 :
            print("Fizz")
        elif num % 5 == 0 and num % 3 != 0 :
            print("Buzz")
        elif  num % 5 == 0 and num % 3 == 0:
            print("FizzBuzz")
        else:
            print(num)
fizzbuzz()            
print(square_integers([1, 2, 3, 4, 5]))
happy_new_year()