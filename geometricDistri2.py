 
def geometricDistribution(n,p):  # For getting the geometric Distribution
    return p*(1-p)**(n-1)

n, d = map(int, input().split())
inspection = int(input())  #At this we need a hit
result = 0
for inspection in range(1,6):
    result = result + geometricDistribution(inspection, n/d)
print("%.3f"%result)