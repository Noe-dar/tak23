import random


target_number = random.randint(0, 100)

while True:
    user_input = int(input("Enter number: "))
    
    if user_input == target_number:
        print("Right!")
        break

    if user_input > target_number:
        print("Target number is lower")
    
    if user_input < target_number:
        print("Target number is higher")
