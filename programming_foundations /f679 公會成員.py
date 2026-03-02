n,Q=map(int,input().split())
m=[int(x) for x in input().split()]
for _ in range(Q):
    
    q=int(input())
    l=0
    yn=False
    r=n-1
    while l<r:
        mid=(l+r)//2
        if m[mid]<q :
            l=mid+1

        else:
            r=mid-1
    if m[mid]==q :
        yn=True





    if yn:print("Yes")
    else:print("No")
        
            
