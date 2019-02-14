# Question 3
# Design an efficient algorithm to reverse an integer
# For example 1234 output 4321

def reverse_integer(n):
    reverse=0
    remainder=0

    while n>0:
        remainder = n%10
        n=n//10
        reverse=reverse*10+remainder

    return reverse

#built in solution

def reverse_int(n):
    return int(str(n)[::-1])

int1 = 54321

print(reverse_integer(4321))

print(reverse_int(int1))