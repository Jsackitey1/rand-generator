# -*- coding: utf-8 -*-
"""
A program to generate a random number to produce a sum and an avearage value across a
range of randomly selected values and determine if the average is greater than the mid value 
in the range

@author: Sackitey Joseph

"""

import random

# Defining varaiables and initializing them
min_value = 1
max_value = 100 
tsum = 0
executions = 0

#N number of random numbers to be produced 

N= 10

# Setting the Target value
target_value = 45

#Setting number of attempts for second test
attempts = 0


print(f"Testing random values from {min_value} to {max_value}\n")

print("Random test 1\n")

while executions < N:
    executions += 1
    random_num = random.randint(min_value, max_value)
    tsum += random_num
    average = tsum / executions
    mid_value = (min_value + max_value) / 2
    comparer = average > mid_value
    
        
print(f"executions: {random_num}")    
print(f"average: {average}")
print(f"sum: {tsum}")
print(f"average is greater than mid value in range: {comparer}\n")


# Working on random test 2

print ("Random Test\n")
print(f"target value: {target_value}")

x= 0

while x!=target_value:
    attempts += 1
    x = random.randint(1, 100)
        
print(f"{target_value} was returned in {attempts} attempts.")
