#HANGMAN
#animal variables/guess placeholder
animal_to_guess = 'cow'
empty_animal = ''
all_guesses = (len(animal_to_guess))+3

#initial game text
print('You have ', all_guesses, 'tries to figure out the animal!')

#while loop to set up game/handle number of turns/wrong guesses
while all_guesses > 0:
    fail_counter = 0
    for letter in animal_to_guess:
        if letter in empty_animal:
            print(letter)
        else:
            print("_")
            fail_counter += 1
    if fail_counter == 0:
        print("You guessed the animal wooo!")
        break
    print

    # user inputs
    user_guess = input("Guess a letter:")
    empty_animal += user_guess

    if user_guess not in animal_to_guess:
        all_guesses -= 1
        print("Swing and a miss :[")
        print("You have", + all_guesses, 'more guesses boss')
        if all_guesses == 0:
            print("Sorry champ, better luck next time!")
            print("You wanted to guess this animal:")
            print(animal_to_guess)

