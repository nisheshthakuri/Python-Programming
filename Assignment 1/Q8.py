"""
Q8. Write a Python program to add an item in a tuple.

Author: Nishesh Thakuri
Date: 19 Dec, 2020

"""
tup = ()
num = int(input("Enter the number of items: "))
for i in range(num):
    item = input("Enter item to be added: ")
    tup = tup + (item,)
print(tup)