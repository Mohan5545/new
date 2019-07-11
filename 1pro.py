def longest(m,n):
  if(m in n):
     return m
  else:
     return longest(m[0:len(m)-1],n)
num=int(input())
char=[]
for _ in range(0,num):
   char.append(input())
char.sort()
print(longest(char[0],char[num-1]))
