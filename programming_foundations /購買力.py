cc,dif=map(int,input().split())
spend=0
x=0
for i in range(cc):
    a,b,c=map(int,input().split())
    arr=[a,b,c]
    if max(arr)-min(arr)>=dif:
        spend+=sum(arr)//len(arr)
        x+=1
        

print(x,spend)
