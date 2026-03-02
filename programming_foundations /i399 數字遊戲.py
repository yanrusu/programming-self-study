a=[int(x) for x in input().split()]
a.sort()
#f=False
#for i in range(0,1):
#    a[i]==[i+1]
#    a.pop(i)
#    f=True
#    break
if a[0]==a[1]==a[2]: print("3",a[1])
elif a[0]==a[1] or a[1]==a[2]:
    print("2",max(a),min(a))
else: print("1",max(a),a[1],min(a))
