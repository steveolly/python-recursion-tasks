# 2. Beginner to Intermediate — Sum of Digits
# Easy–Medium
# Suggested time: 15–20 minutes

# Problem

# Write a recursive function sum_digits(n) that returns the sum of all digits in a non-negative integer.

def sum_of_digits(n):
    if n == 0:
        return 0

    rem = n % 10
    digit = n // 10

    return rem + sum_of_digits(digit)


print(sum_of_digits(0))
print(sum_of_digits(9))
print(sum_of_digits(50))
print(sum_of_digits(507))
print(sum_of_digits(1234))
