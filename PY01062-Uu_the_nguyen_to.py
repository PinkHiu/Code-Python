import math

def checkNguyenTo(n):
    if n == 2: return True
    if n < 2 or n % 2 == 0: return False
    for i in range(3, math.isqrt(n) + 1, 2):
        if n % i == 0: return False
    return True

def check(s):
    count = 0
    if not checkNguyenTo(len(s)): return False
    for c in s:
        if c == '2' or c== '3' or c == '5' or c == '7':
            count += 1 
    if count <= len(s) - count: return False
    return True

"""Main"""
t = int(input())
while t > 0:
    if check(input()): print("YES")
    else: print("NO")
    t -= 1