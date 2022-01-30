A = [2, 1, 3]

n, mod = len(A), 10**9 + 7
left_min, right_min= [0] * n, [0] * n
left_sum, right_sum= [0] * n, [0] * n

s1= []

for i, num in enumerate(A):
    count = 1
    s = num
    while s1 and s1[-1][0] > num:
        n, c = s1.pop()
        count += c
        s += n 
    left_min[i] = count
    left_sum[i] = s
    s1.append([num, count])

s1 = []
for i, num in list(enumerate(A))[::-1]:
    count = 1
    s = num
    while s1 and s1[-1][0] > num:
        n, c = s1.pop()
        count += c
        s += n 
    right_min[i] = count
    right_sum[i] = s
    s1.append([num, count])



print(sum(l * r * (ls + rs - a) for l, r, ls, rs, a in zip(left_min, right_min, left_sum, right_sum, A)))
