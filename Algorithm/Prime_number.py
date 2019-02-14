#Question 9
#Identify if number is prime


class primo:

    def __init__(self, num):
        self.num = num

    def prime_number(self):
        if (self.num < 1):
            print("number must be greater than 0")
            return False

        if (self.num % 2) == 0:
            print("Number is not a prime: ", self.num)

        else:
            print("Number is prime: ", self.num)


t = primo(23)
t.prime_number()
