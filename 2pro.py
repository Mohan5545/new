m,key=input().strip().split(" ")
key=int(key)
i=0
while i<len(m)-1 and key:
	if(m[i]>m[i+1]):
		key-=1
		m=m[:i]+m[i+1:]
		if(i!=0):
			i-=1
	else:
		i+=1
sub=m[:len(m)-key]
print(sub)
