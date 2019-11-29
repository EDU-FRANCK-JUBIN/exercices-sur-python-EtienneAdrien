from math import factorial

res = 0

for n in range(0, 50 + 1):
    res += 1 / factorial(n)

print(res)