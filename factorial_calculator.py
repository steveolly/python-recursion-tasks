# 1. Beginner — Factorial Calculator
# Easy
# Suggested time: 10–15 minutes

# Problem

# Write a recursive function factorial(n) that returns the factorial of a non-negative integer.

# The factorial of a number is the product of all positive integers from 1 to that number.

def factorial(n):
    try:
        if n == 0:
            return 1
        if n < 0:
            return "Not allowed"
        return n * factorial(n-1)
    except ValueError:
        return "Not allowed"


print(factorial(5))
print(factorial(4))
print(factorial(1))
print(factorial(0))
print(factorial(-5))
