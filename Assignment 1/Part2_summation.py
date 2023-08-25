# Write a program that uses a loop to compute and print the sum of all even numbers between 2 and 100 (inclusive).
sum = 0

for i in range(2, 101):
    if i % 2 == 0:
        sum += i
        
print(sum)