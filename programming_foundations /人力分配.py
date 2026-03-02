a1,b1,c1=map(int,input().split())
a2,b2,c2=map(int,input().split())
p=int(input())
m=0
marr=[]
#for i in range(0,p):
for i in range(0,p+1):
    f1=0;f2=0
    f1= a1 * i**2 + b1 * i +c1
    f2= a2 * (p-i)**2 + b2 * (p-i) +c2
    #if f1+f2 > m: m=f1+f2
    marr.append(f1+f2)
print(max(marr))
#print(m)

