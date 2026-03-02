n=[int(x) for x in input().split()]
a=set(n)
if len(n)-len(a)==2:
    a=list(a)
    a.sort(reverse=True)
    print(3,*a)
elif len(n)-len(a)==1:
    a=list(a)
    a.sort(reverse=True)
    print(2,*a)
else:
    a=list(a)
    a.sort(reverse=True)
    print(1,*a)
