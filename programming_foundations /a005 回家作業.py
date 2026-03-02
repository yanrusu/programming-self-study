while True:
    try:
        for i in range(int(input())):
            a=[int(x) for x in input().split()]
            if a[1]-a[0]==a[2]-a[1]:
                print(*a+[a[-1]+a[-1]-a[-2]])
            else:
                print(*a+[a[0]*((a[-1]/a[-2])**4)])
    except:break
