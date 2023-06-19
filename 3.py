N = int(input())
i = 0
n = 0
while 2 ** i < N:
    n = 2 ** i
    print(n)
    i += 1