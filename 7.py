p=10
for n in range(1,7):
    for a in range(1,n+1):
        print(a,end="")
    for l in range(p,0,-1):
        print(" ",end='')
    for h in range(n,0,-1):
        print(h,end='')
    p-=2
    print()
p=0
for n in range(6,0,-1):
    for a in range(1,n+1):
        print(a,end='')
    for s in range(p,0,-1):
        print(" ",end='')
    for o in range(n,0,-1):
        print(o,end='')
    p+=2
    print()
input()
