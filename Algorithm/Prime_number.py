#Question 9
#Identify if number is prime


def prime_number(num):
    if (num < 1):
        print("number must be greater than 0")
        return False

    if (num % 2) == 0:
        print("Number is not a prime: ", num)

    else:
        print("Number is prime: ", num)

prime_number(9007)