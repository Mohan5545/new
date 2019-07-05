n=str(input())
list1=list(n)
list2=[]
for i in range(0,len(list1)):
    if(i%2==0):
        list2.insert(i+1,list1[i])
    elif(i%2==1):
        list2.insert(i-1,list1[i])
print(''.join(list2))
