str = input("str: ")

if len(str) > 7 and len(str) % 2 == 0:
    chars = [*str]
    print(chars[round(len(chars) / 2)])