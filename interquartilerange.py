def median(x):
    n = len(x)
    if n % 2 == 1:
        return x[n // 2]
    else:
        return (x[n // 2 - 1] + x[n // 2]) // 2

n=int(input())
x = list(map(int, input().split()))
f = list(map(int, input().split()))
rage = []
for i in range(n):
    for j in range(f[i]):
        rage.append(x[i])

rage = sorted(rage)
print(rage)

Q2 = median(rage)
if n % 2 == 1:
    q1 = median(rage[0:(n // 2)])
    q3 = median(rage[(n // 2) + 1:])
else:
    q1 = median(x[0:(n // 2)])
    q3 = median(x[(n // 2):])

print(q1)
print(q3)
