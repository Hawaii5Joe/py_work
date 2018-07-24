#zip() returns a list of tuples
#using 'dict' to coerce the list of tuples to a dictionary
# ---------------------------------------------------------------------
names = ["Aliyah", "Bob", "Cathy", "Dan", "Ed", "Frank", "Darnell" 
    "Gary", "Shanice", "Irene", "Jack", "Kelly", "Demetrius"]
ages = [20, 21, 18, 18, 19, 20, 20, 19, 19, 19, 22, 19, 30]
#using dict/zip to coerce data into dictionary
dict_names_ages = dict(zip(names, ages))
print(dict_names_ages)
# ---------------------------------------------------------------------
#guess count
guesses_allowed = 5
#while loop will continually run, until if statements below break the truthfulness
while True:
    #the logic the while loop will run until broken, asking for user inputted name/capitalizing it and storing as a variable
    what_the_user_guessed = input('Enter a name to get their age: ').capitalize()
    #with each pass through the while loop, decrementing the guesses_allowed variable 1
    guesses_allowed -= 1

    #while exit scenarios, happy path = name guessed, sad path = name not guessed
    #if logic to handle a wrong guess, and when there are no more guesses left
    if what_the_user_guessed not in dict_names_ages and guesses_allowed == 0:
        print('There is no one named ', what_the_user_guessed, ' here!')
        #breaking out of the while loop
        break
    # if logic to handle a correct guess
    if what_the_user_guessed in dict_names_ages:
        #using the correct key, return the corresponding value - age, and store as a variable
        age_dict = dict_names_ages[what_the_user_guessed]
        #print the stored age variable as requested
        print(what_the_user_guessed, 'is', age_dict, 'years old!')
        #breaking out of the while loop
        break



