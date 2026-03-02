n,k=map(int,input().split())
a=[int(x) for x in input().split()]+[0]
n1=n+1
ai=[False]*n1
mal=0
nal=0
for i in range(len(a)):
    if ai[i]== True :
        print("j")
        continue
    if a[i]==1:
        alen=0
        print("i")
        a1=a[i]#1
        ai[i]=True
        while a1!=0:
            i+=1
            a1=a[i]#0
            ai[i]=True
            alen+=1
        alen-=1
        b=[]
        b.append(alen)
        mal+=max(b)
        nal+=min(b)

print(mal)
print(nal)
