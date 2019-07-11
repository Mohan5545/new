m=int(input())
m=list(map(int,input().split()))
m.sort()
m.reverse()
if m[0]==0:
    print("0")
else:
    for l in m:
        print(l,end='')
