m=int(input())
a=list(map(int,input().split()))
b=[]
for i in range(m):
    if a[i]==i:
        b.append(i)
        b.sort()
if(len(b)==0):
    print("-1")
else:
    print(" ".join(map(str,b)))
