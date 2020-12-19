"""
Q2. We have v=u+at, where v is velocity, u is initial velocity, and t is the time. And value for each is as
follows: v=25m/s. u=0m/s, t=10 seconds. Find the acceleration a. [Rearrange the equation, also use
proper formatting syntax while displaying the answer.]
Author: Nishesh Thakuri
Date: 18th Dec, 2020
"""
v = int(input("Enter Velocity: "))
u = int(input("Enter Initial velocity: "))
t = int(input("Enter Time: "))
a = (v-u)/t
print("The acceleration is {} meter per second square.".format(a))