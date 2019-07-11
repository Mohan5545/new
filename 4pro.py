m,n=map(str,input().split())
y=0
if len(m)>len(n):
	m,n=n,m
p=0
while p<len(m):
	  y+=(ord(n[p])-ord(m[p]))
	  p+=1
for p in range(p,len(n)):
	  y+=ord(n[p])-ord('a')+1
print(y)
