m,n=map(int,input().split())
r=[int(x) for x in input().split()]
rd=dict();c=0
for i in range(n):
    if r[i] in rd:
        rd[r[i]]+=1
    else:
        rd[r[i]]=1

    if i>=m:
        if rd.get(r[i-m])>1:
            rd[r[i-m]]-=1
        else:
            del rd[r[i-m]]

    if len(rd)==m: c+=1
print(c)
