"""
Q4. Write a python script to demonstrate at least 10 built in functions in Python.
Author: Nishesh Thakuri
Date: 18 Dec, 2020
"""
a="Hello, I am python!"
print(len(a))

print (min(2,3,5))

print (max('a','c','b'))

b=[4/3, 2/3, 1/3, 1/3, 1/3]
print (sum(b))

x= True
print(type(x))

y= 2
print(type(y))

x=int(input("\nEnter a number to check it's absolute value: "))
abs_value=abs(x)
print(f"The absoulte value of number {x} is {abs_value}.")

binary_val = bin(x)
print(f"The binary value of number {x} is {binary_val}.")
print("The value {} is greater than 0:  {}".format(x , bool((x)>0)))

y= int (5)
z= int(5)
power=pow(y,z)
print(f"The value of {y} raised to the power of {z} is {power}.")

list_1=[1,2,3,3,4,5]
print("\nThe intitial order of list is: {}.".format(list_1))
list_1.sort()
print("The sorted list is: {}.".format(list_1))