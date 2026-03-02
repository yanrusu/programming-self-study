n=int(input())
b=[]
c=[]
a=[]
bcount=0
ccount=0
while n>0:
    d=n%10
    a.append(d)
    n//=10
for i in range(0,len(a),2):
    b.append(a[i])
for i in range(len(b)):
    bcount+=b[i]
for i in range(1,len(a),2):
    c.append(a[i])
for i in range(len(c)):
    ccount+=c[i]
print(abs(bcount-ccount))
