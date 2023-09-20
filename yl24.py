def upc(code: str) -> int:
    digts = [int(n) for n in code]
    odd = [digt for digt in digts if digt % 2 == 0]
    even = [digt for digt in digts if digt % 2 != 0]
    
    even_sum = sum(even)
    odd_sum = sum(odd)

    result = odd_sum * 3 + even_sum
    m = result % 10

    if m == 0:
        return m
    else:
        return 10 - m
    
print(
    upc("03600029145")
)