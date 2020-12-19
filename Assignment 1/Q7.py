"""
Q7. Write a Python program to calculate a dog's age in dog's years.
Note: For the first two years, a dog year is equal to 10.5 human years. After that, each  dog year equals 4 human years.
Expected Output:
Input a dog's age in human years: 15
The dog's age in dog's years is 73

Author: Nishesh Thakuri
Date: 19 Dec, 2020
"""
dog_age= int(input("Enter dog's age in human's years:"))

if (dog_age <= 2):
    age = dog_age * 10.5
    print("The age of dog in dog's years is {}".format(age))
else:
    age=(2*10.5)+((dog_age-2)*4)
    print("The dog's age in dog's years is {}".format(age))