import random
chance = 100
gifts = 0
isWin = True
while isWin:
    message = input()
    if message == "Glitch or gifts":
        if random.randint(0, 100) < chance:
            gifts += 1
            chance -= 5
            print(f"You win, your gifts: {gifts} and chance: {chance}%")
        else:
            print("You lose")
            isWin = False
    else:
        print("Enter correct message")