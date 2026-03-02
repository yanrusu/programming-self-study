def f(i):
    if i>=101:
        return i-10
    else :
        return f(f(i+11))

while True:
    t=int(input())
    if t==0: break
    print(f"f91({t}) = {f(t)}")
