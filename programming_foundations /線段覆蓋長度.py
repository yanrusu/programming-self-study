t=int(input())
l=[];ll=[0]*9999999
for i in range(t):
    l.append([int(x) for x in input().split()])


for i in range(t):
    for j in range(l[i][0],l[i][1]):
        ll[j]=1
        
            


print(sum(ll))
