t=int(input())
for i in range(t):
    q,p=map(int,input().split())
    tot=q*p
    if q>1000:
        tot-=tot/10  #10% of the total price
    print('%.6f'%tot)