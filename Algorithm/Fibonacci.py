#Question 10
#Fibonacci sequence problem

def fibonacci(num):
    a,b = 0,1
    for i in range (0, num):
        print(a)
        a,b = b, a + b
    return a

fibonacci(10)

