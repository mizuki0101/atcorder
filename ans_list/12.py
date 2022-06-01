def gcd(a,b):
    while b:
        a, b = b, a % b
    return a

def icm(a,b):
    return a * b / gcd(a,b)

A,B = map(int, input().split())

print(int(icm(A,B)))

# https://atcoder.jp/contests/abc148/tasks/abc148_c