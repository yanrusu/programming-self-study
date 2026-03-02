n=int(input())
num=list(set([int(x) for x in input().split()]))
num+=[0]
for i in range(1,n+1):
    if i!=num[i-1]:
        print(i)
        break

