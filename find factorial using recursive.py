from math import factorial


#factorial n = n * factorial(n-1)
def factorial_recursive(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n*factorial_recursive(n-1)
# f = factorial_iter(5)
f = factorial_recursive(5)
print(f)
