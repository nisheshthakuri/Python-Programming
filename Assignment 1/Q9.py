"""
Q9. Write a Python program to calculate the length of a string. Do not use built-in len() function.

Author: Nishesh Thakuri
Date: 19 Dec, 2020

"""
str_1 = input("Enter a String: ")
count_str_1 = 0
for each in str_1:
    count_str_1 += 1
print(f"The length of string {str_1} is : {count_str_1}")
