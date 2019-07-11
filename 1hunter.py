m=int(input())
n=list(map(int,input().split()))
c=0
d=[]
for i in range(0,m+1):
    if(n.count(i)>1):
      d.append(i)
if(len(d)==0):
    print("unique")
e=sorted(d)
print(' '.join(map(str,e)))
