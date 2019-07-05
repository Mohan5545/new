m,n=map(int,input().split())
z = 0
for i in range(m,n+1):
   if i>1:
        for x in range(2,i):
            if i%x==0:
             break
        else:
          z+=1       
print(z)
