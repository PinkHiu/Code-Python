s = input()
s1 = set()
for i in range(0, len(s), 2):
    if i == len(s) - 1: break
    if s[i: i + 2] in s1: continue
    else: 
        s1.add(s[i:i + 2])
for x in sorted(s1):
    print(x, end = ' ')