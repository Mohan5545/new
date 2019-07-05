m,n=map(list,input().split())
count=0
if(len(m)==len(n)):
    for i in range(0,len(m)):
      if(m[i]==n[i]):
        continue
      else:
        count=count+1
if(count==1):
  print("yes")
else:
  print("no")
