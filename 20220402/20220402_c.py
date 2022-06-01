#N,K,X = map(int, input().split())
#
#item = list(map(int, input().split()))
#
#ans = 0
#coopon = 0
#
#while coopon < K:
#    for i in range(N):
#        while item[i] > X:
#            item[i] -= X
#            print(item[i])
#            coopon += 1
#            ans += item[i]
#
#print(ans)

N,K,X = map(int, input().split())
item = list(map(int, input().split()))

for i in range(N):
    if item[i] // X <= K:
        K -= item[i] // X
        item[i] -= (item[i]//X) * X
    else:
        item[i] -= K*X
        K = 0

item.sort(reverse=True)

for i in range(N):
    if 1<=K:
        item[i]=0
        K-=1
    else:
        break

print(sum(item))

#https://atcoder.jp/contests/abc246/tasks/abc246_c