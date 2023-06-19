n = int(input())
a = []
i = 0
count_1 = 0
count_0 = 0
while i < n:
    b = int(input())
    a.append(b)
    i += 1
for h in range(n):
    if a[h] == 1:
        count_1 += 1
    else:
        count_0 += 1
if count_1 < count_0:
    print(count_1)
else:
    print(count_0)