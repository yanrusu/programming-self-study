a=[int(x) for x in input().split()]
am=a.pop(0)
a.sort()
print(a[0],a[-1],end=" ")
if a[-1]-a[0]==am-1:
    print("yes")
else :
    print("no")
