#mastermind

import random

print("Welcome to mastermind\n")
colours = ['red', 'green', 'blue', 'orange', 'purple', 'yellow']
print("Possible colours (each colour can only appear once):\nblue, green, orange, purple, red, yellow\n")

Combination = []
for i in range(4):
    random_colour = random.choice(colours)
    Combination.append(random_colour)
    colours.remove(random_colour) #computer won't have duplicate colours

turn_counter = 0

def guessing(turn_counter):

    if turn_counter >= 12:
        print("You have run out of turns")
    else:
        print("You are on turn " + str(turn_counter) + "/12\n")
        print("R means you have a correct colour in a correct place")
        print("W means you have a correct colour in an incorrect place\n")

    user_colour_guess = input("Please guess and type in 4 colours, each seperated by a space\ne.g. red yellow orange purple\n")
    user_colour_guess = user_colour_guess.lower()
    user_colours_list = user_colour_guess.split()
    #assuming the user inputs the data correctly

    turn_counter += 1

    feedback = []

    for colour in range(4):
        for guess in range(4):
            if user_colours_list[guess] == Combination[colour]:
                if guess == colour:
                    feedback.append("R") #correct colour in correct place
                else:
                    feedback.append("W") #correct colour, incorrect place
            else:
                continue

    if feedback[0] == 'R' and feedback[1] == 'R' and feedback[2] == 'R' and feedback [3] == 'R':
        print("You guessed correctly!\n")
    else:
        print(feedback)
        guessing(turn_counter)

guessing(turn_counter)
    
