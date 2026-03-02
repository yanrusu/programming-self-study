n,m,w=map(int,input().split())
s=[];tem=[]
for i in range(1,m*n+1):
    tem.append(i)
    if i%m==0:
        s.append(tem)
        tem=[]
even=w//2
if w%2:
    odd=w//2
else:
    odd=w//2-1
    
t1=[[0]*m for i in range(n)]
for i in range(n):
    for j in range(m):
        i1=i+odd;j1=j+even
        i1%=n;j1%=m
        t1[i1][j1]=s[i][j]
        
for i in range(n):
    print(*t1[i])
