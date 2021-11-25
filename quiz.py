# quiz

# functions
# -------------------------
def new_game():
    
    guesses = []
    correct_answers = 0
    question_num = 1

    for key in questions:
        print("---------------------")
        print(key)
        for i in options[question_num - 1]:
            print(i)
        guess = input("Enter (A, B, C, D): ").upper()
        guesses.append(guess)
        
        correct_answers += check_answer(questions.get(key), guess)
        question_num += 1

    display_score(correct_answers, guesses)

# -------------------------
def check_answer(answer, guess):
    
    if answer == guess:
        print("CORRECT!")
        return 1
    else:
        print("WRONG!")
        return 0

# -------------------------
def display_score(correct_answers, guesses):
    print("------------------")
    print("RESULTS")
    print("------------------")
    print("Answers: ", end="")
    for i in questions:
        print(questions.get(i), end=" ")
    print()

    print("Guesses: ", end="")
    for i in guesses:
        print(i, end=" ")
    print()

    score = int((correct_answers/len(questions)) * 100)
    print("Your score is " + str(score) + "%")

# -------------------------
def play_again():
    
    response = input("Do you want to play again? (yes or no): ")
    response = response.upper()

    if response == "YES":
        return True
    else:
        return False
# -------------------------

# variable to hold questions and answers
questions = {
    "Who create python?: " : "A",
    "Is the earth round?: " : "B"
}

options = [
    ["A. Guido van Rossum", "B. Elon Musk", "C. Bill Gates"],
    ["A. False", "B. True", "C. What's earth"]
]

# main function
new_game()

while play_again():
    new_game()

print("Game Over!!")