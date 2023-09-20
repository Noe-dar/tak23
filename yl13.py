animal = input("animal: ")
print([*animal][0])

animals = ["Dog", "Cat", "Cow"]
animals.append(animal)

print(animals)

chars = [*animals[len(animals) - 1]]
print(chars[len(chars) - 1])