"""
Q6. Write a Python program to replace the last element in a list with another list.
Sample data : [1, 3, 5, 7, 9, 10], [2, 4, 6, 8]
Expected Output: [1, 3, 5, 7, 9, 2, 4, 6, 8]

Author: Nishesh Thakuri
Date: 19 Dec, 2020
"""

list_1 = [1, 3, 5, 7, 9, 10]
list_2 = [2, 4, 6, 8]
list_1[-1:] = list_2
print(f"New list: {list_1}")