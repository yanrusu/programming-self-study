def c(n):
    global t,tem,s
    if len(t[n-1])==1:
        return 1
        
        
    else :
        for i in range(t[n-1][0]):
            tem.append(c(t[n-1][i]))


        a=max(tem)
        for x in range(t[n-1][0]):
            del tem[x]

        return a+1






l=int(input())
t=[]
r=[]
s=[]
tem=[]
for i in range(l):
    t.append([int(x) for x in input().split()])
    r+=t[i][1:]
sr=0
for i in range(1,l+1):
    sr+=i
    
r=sr-sum(r)
sum_=c(r)

print(r)
print(c(r))
 
