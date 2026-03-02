n,m,k=map(int,input().split())
n=[i for i in range(1,n+1)]
index=0
for i in range(k):
    index+=m-1
    if index>=len(n):
        index=index%len(n)
    del n[index]
        
if index>=len(n): index=index%len(n)

print(n[index],end="\n")

