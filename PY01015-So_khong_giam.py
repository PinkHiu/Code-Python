def check(s):
    for i in range(len(s) - 1):
        if s[i] > s[i + 1]: return False
    return True

"""Main"""
t = int(input())
while t > 0:
    s = input()
    if check(s): print("YES")
    else: print("NO")
    t -= 1