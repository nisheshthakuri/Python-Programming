"""
Q5. Write a Python program to sum all the items in a list. Do not use built-in sum() function.
Author: Nishesh Thakuri
Date: 18 Dec, 2020
"""
num = int(input("Enter number of items in the list: "))
list_1 = []
for each in range(num):
    item = int(input("Enter item: "))
    list_1.append(item)
sum_items = 0
for each in list_1:
    sum_items += each
print(f"the sum of all the items in the list {list_1} is : {sum_items}")