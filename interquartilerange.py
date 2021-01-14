import statistics as st

n=int(input()) # No. of elements of the arrays.
x = list(map(int, input().split()))
f = list(map(int, input().split()))
rage = []
for i in range(n):
    for j in range(f[i]):
        rage.append(x[i])

rage = sorted(rage)
med=st.median(rage)
q1,q3 = [],[]  # For spliting into half.
for i in rage:
	if(i>med):
		q3.append(i)
	elif(i<med):
		q1.append(i)

q1 = st.median(q1)
q3 = st.median(q3)

print(abs(q1-q3))
