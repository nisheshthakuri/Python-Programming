"""
Q1. The volume of a sphere with radius r is (4/3)*π*r^3. What is the volume of a sphere with radius 5?
Author: Nishesh Thakuri
Date: 18th Dec, 2020
"""
import math

radius = int(input("Enter the radius of sphere: "))

volume = (4/3)*math.pi*radius**3
print("The volume of a sphere with radius {1} is {0} cubic meter.".format(volume,radius))