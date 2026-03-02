n,m=map(int,input().split())
d3=[]
s3=[]
oa=0
for i in range(n):
    tem=[int(x) for x in input().split()]
    oo=max(tem)
    oa+=oo
    d3.append(oo)

print(oa)
for i in range(len(d3)):
    if oa%d3[i]==0:
        s3.append(d3[i])
        
if len(s3)==0: print(-1)
else :print(*s3)
