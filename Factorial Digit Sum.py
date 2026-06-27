def factorial(n):
    if n == 1 or 0:
        return 1
    elif n == 2:
        return 2
    else:
        return n * factorial(n-1)
lst = [int(i) for i in str(factorial(100))]
result = 0
for x in range(len(lst)):
    result = result + lst[x]
print(result)