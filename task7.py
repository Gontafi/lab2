def election(x: bool, y: bool, z: bool) -> bool:
    return True if x + y + z > 1 else False


inp = input().split()
x = bool(int(inp[0]))
y = bool(int(inp[1]))
z = bool(int(inp[2]))

print(int(election(x,y,z)))