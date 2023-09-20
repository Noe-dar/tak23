a = float(input("a: "))
b = float(input("b: "))
c = float(input("c: "))

sides = [a, b, c]

if(len(set(sides)) == 1):
    print("equilateral")
elif(len(set(sides)) == 2):
    print("isosceles")