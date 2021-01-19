from math import factorial
def binomdistri(n,x,p):  #Formula:
    ncr = factorial(n)/(factorial(n-x)*factorial(x))
    rst = (p**x)*(1-p)**(n-x)
    return ncr*rst

p, n = map(int, input().split())
p = p/100
result2 = 0
result1 = binomdistri(n,0,p) + binomdistri(n,1,p) + binomdistri(n,2,p)
for i in range(2,n+1):
    result2 = result2+binomdistri(n,i,p)
print("%.3f"%result1)
print("%.3f"%result2)