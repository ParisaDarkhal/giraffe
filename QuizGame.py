print("Welcome to this computer quiz.")
confirmation = input("Do you want to start a quiz?\n").lower()
if confirmation != "yes":
    print("See you later!")
    quit()

score = 0
questions = 0
answer = input("What is the capital of Canada?\n").lower()
questions += 1
if answer == "ottava":
    score += 1
    print("Correct!")
else:
    print("Incorrect!")
    print("it is Ottava.")

answer = input("What is the capital of Brazil?\n").lower()
questions += 1
if answer == "brasilia":
    score += 1
    print("Correct!")
else:
    print("Incorrect!")
    print("it is Brasilia.")

answer = input("What is the biggest lake in the world?\n").lower()
questions += 1
if answer == "caspian sea":
    score += 1
    print("Correct!")
else:
    print("Incorrect!")
    print("it is Caspian sea.")

answer = input("What is the longest river in the world?\n").lower()
questions += 1
if answer == "nile":
    score += 1
    print("Correct!")
else:
    print("Incorrect!")
    print("it is Nile.")

print("You got " + str(score) + " answers correct out of " + str(questions) + ".")

