def digitsum(n):
    tmp = str(2 ** n)
    sumd = 0
    for x in range(len(tmp)):
        sumd = sumd + int(tmp[x])
    return sumd
i = 1000
print(digitsum(i))