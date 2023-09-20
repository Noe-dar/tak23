fruits = ["Apple", "Orange", "Plum"]
print(fruits)

fruits.append("Pear")
print(fruits[len(fruits) - 1])

fruits[0] = "Melon"
print(fruits)

print("Apple" in fruits)
print(len(fruits))

fruits.remove("Orange")
print(fruits)

fruits.reverse()
fruits.sort()
print(fruits)