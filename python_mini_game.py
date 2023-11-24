print("Welcome to the PythonQuiz Game!\n")

ready = input("ARE YOU READY? ")
score = 0
total_questions = 5

if ready.lower() == "yes":
    answer = input('Question 1: Lists is mutable in python? (True or false) ')
    if answer.lower() == "true":
        score += 1
        print("correct! :)")
    else:
        print("Wrong Answer! :(")

    answer = input('Question 2: Which built-in function can get information from the user? ')
    if answer.lower() == "input" or answer.lower() == "input()":
        score += 1
        print("correct! :)")
    else:
        print("Wrong Answer! :(")

    answer = input('Question 3: Which keyword do you use to loop over a given list of elements? ')
    if answer.lower() == "for" or answer.lower() == "while":
        score += 1
        print("correct! :)")
    else:
        print("Wrong Answer! :(")

    answer = input('Question 4: Is python an object oriented programming language? (True or False) ')
    if answer.lower() == "true":
        score += 1
        print("correct! :)")
    else:
        print("Wrong Answer! :(")

    answer = input('Question 5: Which keyword used to create a function in python? ')
    if answer.lower() == "def" or answer.lower() == "def()":
        score += 1
        print("correct! :)")
    else:
        print("Wrong Answer! :(")

    print('\nThankyou for Playing this small quiz game, you attempted', score, "questions correctly!\n")

    mark = (score / total_questions) * 100
    print('Marks obtained:', mark)

elif ready.lower() == "no":
    print("\nNo problem, just take your time to review and come back again\n")
else:
    print("\nPlease enter yes or no!\n")

print('BYE!')