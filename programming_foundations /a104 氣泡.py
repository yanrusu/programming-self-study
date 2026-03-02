while True:
    try:
        n=int(input())
        list1=[int(x) for x in input().split()]
        for i in range(n,0,-1):
            for j in range(0,i-1):
                if list1[j]>list1[j+1]:
                    list1[j],list1[j+1]=list1[j+1],list1[j]
        print(*list1)
    except:break
                
                
