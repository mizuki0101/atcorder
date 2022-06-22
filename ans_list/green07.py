H,W,X,Y = map(int, input().split())

X -= 1
Y -= 1

mas = []
for i in range(H):
    S=input()
    S=list(S)
    mas.append(S)

ans=1

#up
for i in range(1,H):
    if 0 <= X-i < H :
        if mas[X-i][Y] == "#":
            break
        else:
            ans += 1
    
#down
for i in range(1,H):
    if 0 <= X+i < H :
        if mas[X+i][Y] == "#":
            break
        else:
            ans += 1

#left
for i in range(1,W):
    if 0 <= Y-i < W :
        if mas[X][Y-i] == "#":
            break
        else:
            ans += 1

#right
for i in range(1,W):
    if 0 <= Y+i < W :
        if mas[X][Y+i] == "#":
            break
        else:
            ans += 1
            
print(ans)            