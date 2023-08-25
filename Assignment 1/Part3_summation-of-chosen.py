# Write a program that uses a loop to compute and print the sum of all odd numbers between a and b (inclusive), where a and b are entered by the user.

sum = 0
start = int(input("Enter starting number:"))
end = int(input("Enter ending number:"))

for i in range(start, end+1):
    if i % 2 == 0:
        sum += i
        
print(f"Sum of all even numbers from {start} to {end} is {sum}")