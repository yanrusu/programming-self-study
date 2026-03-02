n,m=map(int,input().split())
p=[];ta=float('inf');r=0;c=0
for i in range(n):
    a=[int(x) for x in input().split()]
    if ta>min(a):ta=min(a);r=i;c=a.index(min(a))
    p.append(a)
su=0
s=[r,c]
while True:
    r=s[0];c=s[1]
    su+=ta
    p[r][c]=1000001
    ta=1000001
    if r+1<n :
        if ta>p[r+1][c]:
            ta=p[r+1][c];r1=r+1;c1=c
    if r-1>0 :
        if ta>p[r-1][c]:
            ta=p[r-1][c];r1=r-1;c1=c
    if c+1<m:
        if ta>p[r][c+1]:
            ta=p[r][c+1];r1=r;c1=c+1
    if c-1>0 :
        if ta>p[r][c-1]:
            ta=p[r][c-1];r1=r;c1=c-1
    if ta==1000001:break
    s=[r1,c1]
print(su)
    
