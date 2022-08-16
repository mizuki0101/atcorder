N = int(input())

mou = []

for i in range(N):
    S,T=map(str, input().split())
    T=int(T)
    mou.append([T,S])

mou.sort(reverse=True)
print(mou[1][1])

    
#    s,t = map(str, input().split())
#    S.append(s)
#    T.append(int(t))
    
