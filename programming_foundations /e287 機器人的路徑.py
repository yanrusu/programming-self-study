n,m=map(int,input().split())
p=[];ta=float('inf');r=0;c=0
for i in range(n):
    a=[int(x) for x in input().split()]
    if ta>min(a):ta=min(a);r=i;c=a.index(ta)
    p.append(a)
su=0
su+=ta
s=[r,c]
while True:
    x=[]
    i=[]
    r=s[0];c=s[1]
    ta=float('inf')
    if r+1<n and p[r+1][c]!=1000001:
        if ta>p[r+1][c]:
            ta=p[r+1][c];r=r+1;c=c;p[r][c]=1000001
    if r-1>0 and p[r-1][c]!=1000001:
        if ta>p[r-1][c]:
            ta=p[r+1][c];r=r-1;c=c;p[r][c]=1000001
    if c+1<m and p[r][c+1]!=1000001:
        if ta>p[r][c+1]:
            ta=p[r][c+1];r=r;c=c+1;p[r][c]=1000001
    if c-1>0 and p[r][c-1]!=1000001:
        if ta>p[r][c-1]:
            ta=p[r][c-1];r=r;c=c-1;p[r][c]=1000001
    if ta==float('inf'):break
    su+=ta
    s=[r,c]
print(su)
    
    

