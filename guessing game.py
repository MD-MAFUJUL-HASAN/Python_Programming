from random import randint
for x in range(1,10):
    num = int(input("Enter your number between 1 to 10 = "))
    randomNumber = randint(1, 10)
    if num == randomNumber:
        print("You have won the game.")
    else:
        print("You have lost the game.")
        print("The number was = ",randomNumber)