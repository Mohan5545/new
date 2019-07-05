x=str(input())
listm=list(x)
listn=[]
for i in range(0,len(listm)):
    if(i%2==0):
        listn.insert(i+1,listm[i])
    elif(i%2==1):
        listn.insert(i-1,listm[i])
print(''.join(listn))
