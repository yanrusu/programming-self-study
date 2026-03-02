n,m=map(int,input().split())
a=[];f=[]
for i in range(n):
    a.append([int(x) for x in input().split()])

for i in range(n):
    for j in range(m):
        d=a[i][j]
        dsum=0
        for s in range(n):
            for t in range(m):
                if abs(i-s)+abs(j-t)<=d:
                    dsum+=a[s][t]
        if d%10 == dsum%10:
            f.append([i,j])

x=len(f)
print(x)
for i in range(x):
    print(*f[i])
