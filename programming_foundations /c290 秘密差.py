'''
有很多種做法，用while分奇數偶數，開list、迴圈取餘數分奇數偶數
'''

a=list(input())
o=a[1::2]
e=a[::2]
for i in range(len(o)):
    o[i]=int(o[i])
    e[i]=int(e[i])
e[-1]=int(e[-1])

print(abs(sum(o)-sum(e)))
