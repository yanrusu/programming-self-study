t=int(input())
l=[]
for i in range(t):
    l.append([int(x) for x in input().split()])

'''
for i in range(t):
    for j in range(t-i-1):
        if l[j][0]> l[j+1][0]:
            l[j],l[j+1]=l[j+1],l[j]
            '''

l.sort(key=lambda x: x[0])

now=l[0][1]
sum_=l[0][1]-l[0][0]
for i in range(1,t):
    if l[i][1]>now:
        if l[i][0]<now:
            sum_+=l[i][1]-now
            now=l[i][1]
        else:
            now=l[i][1]
            sum_+=l[i][1]-l[i][0]
print(sum_)
