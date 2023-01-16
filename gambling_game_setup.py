# program will adjust the probability of a number based on the available balance and display random numbers based on
# their probability
import random


# adjust the probability based on account balance
def method_identifier(account_balance):
    adjust = 0
    if 1000 < account_balance <= 10000:
        adjust = 50
    elif 10000 < account_balance <= 100000:
        adjust = 100
    elif account_balance > 100000:
        adjust = 200
    else:
        adjust = 0
    return adjust


# generates random numbers 1 through 5
def generator(factor):
    f = factor
    a = b = c = d = e = 100

    if num == 1:
        a = f
    elif num == 2:
        b = f
    elif num == 3:
        c = f
    elif num == 4:
        d = f
    elif num == 5:
        e = f
    # generates 20 random numbers from 1 through 5 for demonstration
    lucky_number = (random.choices(numbers, weights=(a, b, c, d, e), k=20))
    print(lucky_number)
    # to show the probability of each number
    # print(a, b, c, d, e)


if __name__ == "__main__":
    # increase balance for high chance of winning and vis versa
    available_balance = 200
    numbers = [1, 2, 3, 4, 5]
    num = int(input("Choose number from 1 through 5: "))
    generator(method_identifier(available_balance))
