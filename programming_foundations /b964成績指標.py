n=input()
a=[int(x) for x in input().split()]
b=[]
c=[]
ac=sorted(a)
print(*ac)
for i in a:
    if i>=60: b.append(i)
    else: c.append(i)

if b==[]:
    print(max(c))
    print('worst case')
elif c==[]:
    print('best case')
    print(min(b))
else:
    print(max(c))
    print(min(b))
