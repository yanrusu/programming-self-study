a,b = map(int,input().split())
x=[int(x) for x in input().split()]
p=x[0]
have=True
earn=0
y=-x[0]
for i in range(len(x)):
    if have:
        if x[i] >= p+b:
            earn=x[i]-p
            y+=x[i]
            p=x[i]
            have=False
    else:
        if x[i]<=p-b:
            p=x[i]
            y-=x[i]
            have=True
if have: print(earn)
else: print()
            
            
            
        
