from itertools import permutations
m=input("")
s=permutations(m)
for i in list(s):
    print("".join(i))
