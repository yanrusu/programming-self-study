n=int(input())
a=[0]*n
for i in range(n):
    a[i]=[int(x) for x in input().split()]
mind=300
maxd=0
for i in range(n-1):
    mind1=abs(a[i][0]-a[i+1][0])+abs(a[i][1]-a[i+1][1])
    maxd1=abs(a[i][0]-a[i+1][0])+abs(a[i][1]-a[i+1][1])
    if maxd1>maxd: maxd=maxd1
    if mind1<mind: mind=mind1
print(maxd, mind)
    
