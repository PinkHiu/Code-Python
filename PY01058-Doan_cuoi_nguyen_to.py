import math

def checkNguyenTo(n):
    if n == 2: return True
    if n < 2 or n % 2 == 0: return False
    for i in range(3, math.isqrt(n) + 1, 2):
        if n % i == 0: return False
    return True

"""Main"""
t = int(input())
while t > 0:
    s = input()
    if checkNguyenTo(int(s[-4:])): print("YES")
    else: print("NO")
    t -= 1