def self_powers(n):
    series = 0
    x = 1
    while x <= n:
        series = series + (x ** x)
        x = x + 1
    series = str(series)
    return series[-10:]
print(self_powers(1000))