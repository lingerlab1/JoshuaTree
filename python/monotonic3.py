# A =  [2,3,2,1]
A = [3,1,3]
A = [2, 4, 3, 1, 2, 4, 8]
A0 = [0] + A


stack = []

n = len(A0)

left_bound, right_bound, cum_sum = [None] * n, [None] * n, [0] * n

for i, num in enumerate(A0):
    idx = i
    while stack and stack[-1][1] >= num:
        idx = stack.pop()[0]
        
    stack.append([idx, num])
    left_bound[i] = idx
    
    if i:
        cum_sum[i] = cum_sum[i-1] + num


stack = []

for i in range(n)[::-1]:
    num = A0[i]
    idx = i
    while stack and stack[-1][1] > num:
        idx = stack.pop()[0]
    
    stack.append([idx, num])
    right_bound[i] = idx

res = 0

for idx, (l, r, s) in enumerate(zip(left_bound, right_bound, A0)):
    if s:
        for lower_bound in range(l-1, idx):
            for upper_bound in range(idx, r+1):
                res += (cum_sum[upper_bound] - cum_sum[lower_bound]) * s
                
print(res)