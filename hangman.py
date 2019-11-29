import random



city = ("Warsaw", "Paris", "London", "Rome")
attempt = 6   # list of attempts
new_lottery = []
lottery = ""
#  draw of the city


def draw(city):
    global lottery
    lottery = random.choice(city)  
    lottery = lottery.lower()
    start = input("Wellcome to my first game.You are playing HANGMAN.Choose a european citiy and find the letter.You have six attempt.Click ENTER and play")

    print("The city drawn is:", len(lottery) * '_ ')
    dush = len(lottery) * '_ '


def get_letter():
    global new_lottery
    global dush
    guess_1 = input("select letter:")
    new_lottery.append(guess_1)
    return guess_1


def won():
    won = True
    for letter in lottery:
        if letter not in new_lottery:
            won = False
            break
    return won
    

def main_menu():
    global attempt
    draw(city)
    while not won() and attempt > 0:
        letter = get_letter()

        if letter not in list(lottery):
            attempt -= 1
            print("wrong letter")
        else:
            print("Bravo! you guessed")
            print(letter)
        
        if won():
            print('you won')
            print("The guessed word is:", lottery.upper())
            break
    if attempt == 0:
        print("you lost")

if __name__ == '__main__': 
    main_menu()
