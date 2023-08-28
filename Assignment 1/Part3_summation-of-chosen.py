"""
Summation of chosen range
Lukas Maynard
CS222-1
Assignment 1 Part 3
"""
sum = 0
start = int(input("Enter starting number:"))
end = int(input("Enter ending number:"))

for i in range(start, end+1):
    if i % 2 == 0:
        sum += i
        
print(f"Sum of all even numbers from {start} to {end} is {sum}")