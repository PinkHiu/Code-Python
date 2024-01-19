def check(s):
    if len(s) % 2 == 0: return False
    if s[0] == s[1]: return False
    for i in range(2, len(s), 2):
        if s[i] != s[0]: return False
    return True

"""Main"""
t = int(input())
while t > 0:
    s = input()
    if check(s): print("YES")
    else: print("NO")
    t -= 1