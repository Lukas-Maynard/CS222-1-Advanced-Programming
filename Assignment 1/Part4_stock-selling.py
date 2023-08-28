"""
Stock selling
Lukas Maynard
CS222-1
Assignment 1 Part 4
"""

target = float(input("Enter the target stock price: "))
current = float(input("Enter current stock price: "))

while(current < target):
    current = float(input("Enter current stock price: "))

print("Shares can be sold now")
