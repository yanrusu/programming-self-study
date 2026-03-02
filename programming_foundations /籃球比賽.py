H=[int(x) for x in input().split()]
G=[int(x) for x in input().split()]
H1=[int(x) for x in input().split()]
G1=[int(x) for x in input().split()]
hs=sum(H)
hs1=sum(H1)
Gs=sum(G)
Gs1=sum(G1)
print(hs,":",Gs,sep="")
print(hs1,":",Gs1,sep="")
if hs>Gs and hs1>Gs1:
    print("Win")
elif hs<Gs and hs1<Gs1:
    print("Lose")
else: print("Tie")
