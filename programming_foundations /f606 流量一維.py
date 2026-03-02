n,m,k=map(int,input().split())
s=[int(x) for x in input().split()]
mi=float('inf')
for i in range(k):
    c=input()
    tot=0
    for i in range(m):
        if i==int(c):
            tot+=s[i]*1
           
        else:
        
            if s[i]<=1000:
                tot+=s[i]*3

            else:
                tot+=s[i]*2+1000
    if tot!=0:
        mi=min(tot,mi)

print(mi)
        
