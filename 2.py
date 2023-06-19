S = int(input())
P = int(input())
X = 0
Y = 0
for i in range(S):
    for j in range(P):
        if i + j == S and i * j == P:
            X = i
            Y = j
print(Y, X)