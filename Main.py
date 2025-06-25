print("Welcome to the Quiz...")

playing = input("Do you want to play? ")
print(playing)

if playing.lower() != "yes":
    quit()

print("Okay! Let's play :)")

answer = input("What does CPU stand for? ")
if answer.lower() == "central processing unit":
    print("Correct!")

    score = 0
else:
    print("Wrong!")

answer = input("2. What does RAM stand for? ")
if answer.lower() == "random access memory":
    print("Correct!")
    score += 1
else:
    print("Wrong!")

answer = input("3. What is the keyword to define a function in Python? ")
if answer.lower() == "def":
    print("Correct!")
    score += 1
else:
    print("Wrong!")

answer = input("4. What symbol is used to comment a single line in Python? ")
if answer == "#":
    print("Correct!")
    score += 1
else:
    print("Wrong!")

answer = input("5. Which data type is used to store True or False? ")
if answer.lower() == "boolean":
    print("Correct!")
    score += 1
else:
    print("Wrong!")

answer = input("6. What function is used to get input from the user? ")
if answer.lower() == "input":
    print("Correct!")
    score += 1
else:
    print("Wrong!")

answer = input("7. What is used to repeat a block of code multiple times? (write: for or while) ")
if answer.lower() in ["for", "while"]:
    print("Correct!")
    score += 1
else:
    print("Wrong!")

answer = input("8. What keyword is used to make a decision in Python? ")
if answer.lower() == "if":
    print("Correct!")
    score += 1
else:
    print("Wrong!")

answer = input("9. What type of loop runs only when a condition is true? ")
if answer.lower() == "while":
    print("Correct!")
    score += 1
else:
    print("Wrong!")

answer = input("10. What is the output of print(2 + 3 * 2)? ")
if answer == "8":
    print("Correct!")
    score += 1
else:
    print("Wrong!")

print("You got " + str(score) + " out of 10 questions correct!")
print("You got " + str((score/10) * 100) + "%.")
print("Thanks for playing!")