def fun(i):
    global f
    num=0
    numl=len(str(i))
    a=list(str(i))
    for j in range(numl):
        num+=int(a[j])**numl
    if num==i:
        f.append(i)






n,m=map(int,input().split())
f=[]
for i in range(n,m+1):
    fun(i)

if f:print(*f)
else: print("none")
    
