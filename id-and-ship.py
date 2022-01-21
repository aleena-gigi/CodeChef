t=int(input())
while t>0:
    id=input().lower()
    if id=='d':
        print("Destroyer")
    elif id=='b':
        print("Battleship")
    elif id=='c':
        print("Cruiser")
    elif id=='f':
        print("Frigate")
    t-=1
