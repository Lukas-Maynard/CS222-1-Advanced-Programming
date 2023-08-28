"""
Tuition increase rate
Lukas Maynard
CS222-1
Assignment 1 Part 5
# Having the rate be .015 for 10 interations instead of .03 for 5 gives slightly different results
# (different by around 10) but for estimated values it seems decent enought.  
"""
from math import ceil

Tuition = 8000
rate = .015
print("Estimated Tuition for the next 5 years.")

for i in range(10):
    Tuition += Tuition * rate
    print(f"Year {ceil((i/2)+.5)} Semester {i%2+1} Tuition: ${Tuition:.2f}")