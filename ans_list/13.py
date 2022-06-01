N,X = map(int, input().split())

alc = 0

for i in range(N):
    V,P = map(int, input().split())
    alc += V * P

    if alc > (X*100):
        print(i + 1)
        exit()

print(-1)


# https://atcoder.jp/contests/abc189/tasks/abc189_b
# 少数がでるときは100倍にする
