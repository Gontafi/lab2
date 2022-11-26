def power(a: float, n: int) -> float:
    return a ** n

inp = input().split()
a = float(inp[0])
n = int(inp[1])

print(power(a, n))
