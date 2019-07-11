m=int(input())
n=list(map(int,input().split()))
for i in range(m):
    if(n.count(i)==1):
        print(i)
