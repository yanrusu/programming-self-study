a=[[0]*500002]
a.append([1]*500002)
c=[0,1,5,10,20,50,100,200,500,1000,2000]
for i in range(9):
    a.append([0]*50002)
for i in range(11):
    a[i][0]=1

for i in range(2,11):
    for j in range(1,50002):
       r=0
       while j-c[i]*r>=0:
            a[i][j]+=a[i-1][j-r*c[i]]
            r+=1

            


while True:
    t=[int(x) for x in input().split()]
    t=sum(t)
    if t==0 : break
    c=0
    print(a[10][t]-1)
    
        


        
