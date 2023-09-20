n = input("n: ")

def repeat_and_parse(n, x):
    result = ""
    for _ in range(0, x):
        result += n
    
    return int(result)


print(
    repeat_and_parse(n, 1) + repeat_and_parse(n, 2) + repeat_and_parse(n, 3)
)