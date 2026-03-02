s=[int(x) for x in input().split()]
sc=[0]*(s[0]+1)
sc[0]=s[1]
for i in range(1,len(s)-1):
    sc[i]=sc[i-1]+s[i+1]
    
    
print(max(sc))
