
import random
from turtle import clear
import stages
from wordlist import word_list

chosen_word = random.choice(word_list)



print(f'Pssst, the solution is {chosen_word}.')

lives = 6

display = []

for blank in range(len(chosen_word)):
    display.append("_")
print(display)

end_of_game =  False

while not end_of_game:

    guess = input("Guess a letter: ").lower()

    for position in range(len(chosen_word)):

        letter = chosen_word[position]

        if guess == letter:
            display[position] = letter 

    if guess not in chosen_word:
        lives -= 1

        if lives == 0:

            end_of_game = True
            print("You lose")

    print(f"{' '.join(display)}")

    if "_" not in display:
        end_of_game = True
        print("You win")


print(stages.stages[lives])

