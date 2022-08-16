n,s,d = map(int, input().split())

ans = 0

for i in range(n) :
    x,y = map(int, input().split())
    if s > x and y > d :
        ans += 1
        break
        
if ans == 1 :
    print("Yes")
else:
    print("No")