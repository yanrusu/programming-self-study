a,b=map(int,input().split())
cc=int(input())
dub=0
for i in range(cc):
    arr=[int(x) for x in input().split()]
    a1=0
    b1=0
    for i in range(len(arr)):
        if arr[i]==a: a1+=1
        if arr[i]==b: b1+=1
        if arr[i]==-a: a1-=1
        if arr[i]==-b: b1-=1

    if (a1 and b1)>0:
        dub+=1
    
print(dub)
    
