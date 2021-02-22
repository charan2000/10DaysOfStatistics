import math

mean = float(input())
k = int(input())

pd = mean**k*math.e**(-mean)/math.factorial(k)

print("{:.3f}".format(pd))