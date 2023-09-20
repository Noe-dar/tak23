name = input("Enter your name: ")
print(f"Hello, {name}")

place = input("Enther where you live: ").lower()

if(place == "saaremaa"):
    print("Nice!")


age = int(input("Enter your age: "))

if age < 18:
    print("You too young to drive car")
else:
    print("You can drive car")