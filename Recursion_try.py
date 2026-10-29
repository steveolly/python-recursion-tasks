# def countdown_sum(num):
#     if num < 1:
#         return 0
#     if num % 2 == 0:
#         return countdown_sum(num-1)
#     else:
#         return num + countdown_sum(num-2)


# def fib(n):
#     if n < 2:
#         return n
#     return fib(n-1) + fib(n-2)

# def fib(n,memo=None):
#     if n < 2:
#         return n
#     if memo == None:
#         memo = {}
#     if n in memo:
#         return memo[n]
#     memo[n] = fib(n-1,memo) + fib(n-2,memo)
#     return memo[n]

# print(fib(8))

# def power(base, exp):
#     if exp == 0:
#         return 1
#     return base * power(base, exp-1)


# def reverse_string(s):
#     if s == "":
#         return ""
#     return reverse_string(s[1:]) + s[0]

def is_palindrome(s):
    left = 0
    right = len(s)-1

    if len(s) <= 1:
        return True
    if s[0] == s[-1]:
        return is_palindrome(s[1:-1])
    return False

print(is_palindrome("aeiouoiea"))
print(is_palindrome("a"))
print(is_palindrome("ae"))
print(is_palindrome("aei"))
print(is_palindrome("aeiiea"))
