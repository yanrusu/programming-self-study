   n=int(input())
for i in range(n):
    a=input()
    while True:
        n=a
        a=a[::-1]
        a=a+n
        if n==a:
            print(a)
            break
    
            


