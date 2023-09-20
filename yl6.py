def max(a, b):
    return a if a > b else b

a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))

print(max(a, max(b, c)))