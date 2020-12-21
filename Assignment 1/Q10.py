"""
Q10. Write a Python program to print a specified list after removing the 0th, 4th and 5th elements.
Sample List : ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
Expected Output : ['Green', 'White', 'Black']

Author: Nishesh Thakuri
Date: 19 Dec, 2020
"""
list = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
list.remove('Red')
list.remove('Pink')
list.remove('Yellow')
print(list)
