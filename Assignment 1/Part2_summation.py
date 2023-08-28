"""
Summation
Lukas Maynard
CS222-1
Assignment 1 Part 2
"""
sum = 0

for i in range(2, 101):
    if i % 2 == 0:
        sum += i
        
print(sum)