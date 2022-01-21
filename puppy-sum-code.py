def sum(n):
    s=0
    for i in range(1,n+1):
        s+=i
    return s

t=int(input())
for i in range(t):
    d,n=map(int,input().split())
    while(d>0):
        n=sum(n)
        d-=1
    print(n)