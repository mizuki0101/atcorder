N = int(input())

ten = []
for i in range(N):
    x,y = map(int, input().split())
    ten.append([x,y])

for i in range(N):
    for ii in range(i+1,N):
        for iii in range(ii+1,N):
            if (ten[ii][0] - ten[i][0])*(ten[iii][1] - ten[i][1]) == (ten[iii][0] - ten[i][0])*(ten[ii][1] - ten[i][1]):
                print("Yes")
                exit()
print("No")

#https://atcoder.jp/contests/abc181/tasks/abc181_c