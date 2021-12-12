import random

#Getting guess
def get_guess():
    return list(input("What is your guess"))

#Generate computer code 123
def generate_code():
    digits = [str(num) for num in range(10)]

    # Shuffle the digits
    random.shuffle(digits)
    # Then grab the first three
    return digits[:3]

# Generate the clues
def generate_clues(code, user_guess):
    if user_guess == code:
        return "Code cracked!"

    clues = []

    for ind, num in enumerate(user_guess):
        if num == code[ind]:
            clues.append("Match")
        elif num in code:
            clues.append("Close")

    if clues == []:
        return ["Nope"]
    else:
        return clues

#Game logic

print("Welcome Code Breaker!")

secretCode = generate_code()

clue_report = []

while clue_report != "Code cracked!":

    guess = get_guess()

    clue_report = generate_clues(guess, secretCode)
    print("Here is the result of your guess: ")
    for clue in clue_report:
        print(clue)
