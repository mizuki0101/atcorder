#def divisor_list(i,N):
#    divisor=[]
#    if N ** 0.5 > i:
#        return divisor
#    elif N % i == 0:
#        divisor.append(i)
#        a = N // i
#        divisor.append(i)
#        return divisor
#
#N = int(input())
#
#for i in range(1,N+1):
#    divisor_list(i,N)
#    print(divisor_list)

#https://atcoder.jp/contests/abc180/tasks/abc180_c

def divisor_list(N):
    #約数をリストに追加
    divisor = []
    #１から順にカッ９人
    i = 1
    #ルートから少数が出ないように
    # N**0.5 >= i でもルートは出せる
    while i**2 <= N :
        #あまりが0のときNの約数となる
        if N % i == 0:
            divisor.append(i)
            #値が重複した場合はリストに追加しない
            if i != N//i:
                divisor.append(N//i)
        i+=1
    divisor.sort()
    #戻り値
    return divisor

#入力
N = int(input())

#出力
ans = divisor_list(N)
for i in ans:
    print(i)
    