d=[1,2]
for i in range(2,100):
    d.append(d[i-1]+d[i-2])


while True:
    try:
        # stc=int(input())
        # print(d[stc-1])
        print(d)
        break
        
    except: break
