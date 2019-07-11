n,m=input().split()
char=abs(len(m)-len(n))
for g in range(len(n)):
  if(len(m)==1 and m[g] in n):
    break
  if(n[g]!=m[g]):
    char=char+1
print(char)    
  
