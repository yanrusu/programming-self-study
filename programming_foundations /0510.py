n=int(input())
s=[int(i+1) for i in range(n)]
p=0
while len(s)!=1:
    p+=2
    print(p,s,len(s))
    if p>=len(s):
        p=p%len(s)
        del s[p]
    else :
        del s[p]
print(s[0])
