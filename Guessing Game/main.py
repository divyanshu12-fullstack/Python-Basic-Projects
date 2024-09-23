import random


def guessing_user(x):
    answer = random.randint(1, x)
    flag = True
    counter = 3
    while flag and counter > 0:
        user_response = int(input(f"Guess the number b/w 1 and {x}: "))
        if answer == user_response:
            print("Correct Answer")
            flag = False
        elif answer > user_response:
            print("Too low")
            counter -= 1
        else:
            print("Too High")
            counter -= 1


# Here computer guesses a number, and you provide a feedback
# according to solution which user is thinking about
def computer_guessing(limit):
    low = 1
    high = limit
    feedback = ""
    while feedback != "c" and low <= high:
        # PC's Guess
        computer_ans = random.randint(low, high)
        feedback = input(f"Computer's guess is {computer_ans}. Is it too high (h), too low (l), or correct (c)? ").lower()
        if feedback == "h":
            # Adjust the high boundary if the guess is too high
            high = computer_ans - 1
        elif feedback == "l":
            # Adjust the low boundary if the guess is too low
            low = computer_ans + 1
    if feedback == "c":
        print("Yay!! Computer predicted the correct value.")
    else:
        print("Something went wrong!")


guessing_user(10)
computer_guessing(100)
