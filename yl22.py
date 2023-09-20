from random import choice


def is_win(a, b):
    if a == "rock" and b == "scissors":
        return True
    if a == "scissors" and b == "paper":
        return True
    if a == "paper" and b == "rock":
        return True

    return False

print("To exit, type .exit")

while True:
    user_select = input("rock, paper or scissors: ")
    if user_select == ".exit": break

    computer_select = choice(["rock", "paper", "scissors"])
    print(f"Computer selects {computer_select}")
    if is_win(user_select, computer_select):
        print("You won")
    else:
        print("Computer win")
