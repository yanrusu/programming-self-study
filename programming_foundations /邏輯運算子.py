a,b,c = map(int,input().split())
x=False
if a>0: a=1
if b>0: b=1
if (a and b)==c :
    print("AND")
    x=True
    
if (a or b)==c :
    print("OR")
    x=True
if ((a and not(b)) or (not(a) and b))==c:
    print("XOR")
    x=True
if x==False: print("IMPOSSIBLE")
