while True:
    n=int(input())
    if not n:break
    for i in range(1,n+1):
        if i%7!=0 and i<n and i>0:
            print(i,end=' ')
    print()
