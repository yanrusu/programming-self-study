K,Q,R=map(int,input().split())
a=list(input())
oa=[[0] for i in range(Q)]
for i in range(Q):
    a1=[int(x) for x in input().split()]
    new=[0]*K
    for y in range(len(a1)):
        nindex=a1[y]-1
        new[nindex]=a[y]
    oa[i]=new
    a=new
    
for i in range(R):
    fo=""
    for j in range(Q):
        fo+=oa[j][i]
    print(fo)
        
      
        
