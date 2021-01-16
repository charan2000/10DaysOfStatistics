from math import factorial
def binomdistri(n,x,p):  #Formula:
    ncr = factorial(n)/(factorial(n-x)*factorial(x))
    rst = (p**x)*(1-p)**(n-x)
    return ncr*rst

b,g = map(float, input().split())
p = b/(b+g)
result = 0
for i in range(4):
    result = result+binomdistri(6,i+3,p)
print("%.3f"%result)