y,maxn,minn=map(int,input().split())
c=max(y,maxn,minn)
b=min(y,maxn,minn)
a=(y+maxn+minn)-c-b
if a+b<=c:
    x="No"
elif a*a+b*b<c*c:
    x="Obtuse"
elif a*a+b*b==c*c:
    x="Right"
elif a*a+b*b>c*c:
    x="Acute"
print(b,a,c,sep=" ")
print(x)
