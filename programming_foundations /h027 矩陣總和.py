s,t,n,m,r=map(int,input().split())
A=[];B=[];same=0;sumA=0;min=float("inf")
for i in range(s):
    a=[int(x) for x in input().split()]
    A.append(a)
    sumA+=sum(a)

for i in range(n):
    B.append([int(x) for x in input().split()])


for i in range(n):
    for j in range(m):
        if n-i>=s and m-j>=t:
            r1=0;same+=1;sumB=0
            for i1 in range(s):
                for j1 in range(t):
                    sumB+=B[i+i1][j+j1]
                    if A[i1][j1]!=B[i+i1][j+j1]:
                        r1+=1

            if r1>r:
                same-=1
                sumB=0
            elif sumB and abs(sumB-sumA)<min:
                min=abs(sumB-sumA)
print(same)
if not same:
    print(-1)
else:print(min)
                
                        
            
            
            

        
        
