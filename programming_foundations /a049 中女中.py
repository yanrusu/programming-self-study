while True:
    n=int(input())
    x=0
    for i in range(n):
        for j in range(n):
            if j%3==x:
                print('@',end='')
            else: print('-',end='')
        if x==2 :x=-1
        x+=1
        print()

