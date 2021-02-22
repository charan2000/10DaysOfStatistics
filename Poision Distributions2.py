import math

def E(λ):
    return λ + λ ** 2

λ1, λ2 = map(float, input().split())

print("{:.3f}".format(160 + 40 * E(λ1)))
print("{:.3f}".format(128 + 40 * E(λ2)))