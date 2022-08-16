n,s,d = map(int, input().split())
for i in n :
    x,y = map(int, input().split())
    if s > x and d > y :
        print("Yes")
        break

print("No")