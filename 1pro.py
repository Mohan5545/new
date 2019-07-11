def longest(m,n):
        if(m in n):
            return m
        else:
            return longest(st1[0:len(m)-1],n)
j = int(input())
a= []
for _ in range(0,j):
    a.append(input())
a.sort()
print(longest(a[0],a[j-1]))
