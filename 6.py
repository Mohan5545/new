m1,m2=map(str,input().split())
if(len(m1)!=len(m2)):
    print("no")
x=[m1.count(i) for i in m1]
y=[m2.count(i) for i in m2]

if(x==y):
    print("yes")
else:
    print("no")
