# program will adjust the probability of a number based on the gambling company's account balance 
# display random numbers based on their probability
# update user & gambling company's account
import random
import sys


# user's choice input & validator
def ques(acc, user_bal):
    num = input("Choose number from 1 to 5: ")
    # choice validator
    for z in num:
        if z not in [str(y) for y in (range(1, 6))]:
            print("Invalid choose entered" '\n')
            ques(acc, user_bal)
    playing_rounds(acc, user_bal, int(num))


# playing rounds input & validator
def playing_rounds(owner_acc, user_acc, n):
    pla = input("play times: ")
    for v in pla:
        if v not in [str(y) for y in (range(0, 10))]:
            print("Invalid play time's entered" '\n')
            playing_rounds(owner_acc, user_acc, n)

    adjustments(owner_acc, user_acc, n, int(pla))


# probability adjustors, accounts calculator, choice & random number comparator
def adjustments(acc_balance, user_bala, numb, play):
    mul = input("wager per play: R ")
    # wager validator
    for w in mul:
        if w not in [str(y) for y in (range(0, 10))]:
            print("Invalid wager entered" '\n')
            adjustments(acc_balance, user_bala, numb, play)

    wage = int(mul)
    given = [1, 2, 3, 4, 5]
    a = b = c = d = e = 100
    count = 0

    # probability adjuster, generator & comparator for random number, based on owner's account balance
    while 0 <= count < play and wage > 0:
        count += 1
        if acc_balance <= wage:
            adjust = 0
        elif 1000 < acc_balance <= 10000:
            adjust = 50
        elif 10000 < acc_balance <= 50000:
            adjust = 100
        elif acc_balance > 100000:
            adjust = 150
        elif acc_balance > 150000:
            adjust = 200
        else:
            adjust = 500

        if numb == 1:
            a = adjust
        elif numb == 2:
            b = adjust
        elif numb == 3:
            c = adjust
        elif numb == 4:
            d = adjust
        else:
            e = adjust
        lucky_num = (random.choices(given, weights=(a, b, c, d, e), k=1))

        # user's choice & lucky number comparator and accounts calculator
        for i in lucky_num:

            if user_bala < wage:
                print('\n'"Insufficient balance.")
                user_bb = int(input("load account or enter 0 to withdraw/ change wager: ")) + user_bala
                ques(acc_balance, user_bb)

            elif numb == i and user_bala >= wage:
                acc_balance -= wage
                user_bala += wage
                print("win", end=', ')
                print(lucky_num)

            elif numb != i and user_bala >= wage:
                acc_balance += wage
                user_bala -= wage
                print("loss", end=', ')
                print(lucky_num)
    communicator(acc_balance, user_bala)


# accounts balances, game options and owner's account document updater
def communicator(account_balance, user_balance):
    print('\n' "owner's balance: R", account_balance)
    print("user's balance: R", user_balance)
    play_again = (input('\n'"play again? Y = Yes, N = No or press any key to exit: ")).upper()

    # replay game
    if play_again == 'Y':
        ques(account_balance, user_balance)

    # exit game and owner's account document updater
    elif play_again == 'N':
        print("user's balance withdrawal: R", user_balance)
        print("game closing!!!")
        sys.stdout = open("gambling game.txt", 'w')
        print(account_balance)
        sys.stdout.close()

    # initiates new player
    else:
        print("user balance withdrawal: R", user_balance)
        print("play responsibly, winners know when to quit")
        print('\n' "Next player, Welcome")
        new_player(account_balance)


# new player account loader and validator
def new_player(owner_balance):
    user_b = input("load account balance: R ")
    # user account balance validator
    for x in user_b:
        if x not in [str(y) for y in (range(0, 10))]:
            print("Invalid amount entered" '\n')
            new_player(owner_balance)

    ques(owner_balance, int(user_b))


# opens owner's available balance document & calls new player
if __name__ == "__main__":

    gaming_company = open("gambling game.txt", 'r').read()
    new_player(int(gaming_company))
