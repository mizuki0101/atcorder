N,K = map(int, input().split())

# 2次元配列
friends = []
for i in range(N):
    A,B = list(map(int, input().split()))
    friends.append([A,B])

friends.sort()

# 先に行ける場所まで計算をする
mura = 0
mura += K

# 後から途中で追加される要素を計算する
for i in range(N):
    friend_mura = friends[i][0]
    friend_money = friends[i][1]

    if friend_mura <= mura:
        mura += friend_money
    else:
        break

print(mura)

# https://atcoder.jp/contests/abc203/tasks/abc203_c
