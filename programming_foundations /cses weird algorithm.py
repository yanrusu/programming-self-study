n=int(input())
a=[]
while n != 1:
    a.append(n)
    if n%2==0:
        n=n//2
    else :
        n=n*3+1
a+=[1]        
print(*a)
        
