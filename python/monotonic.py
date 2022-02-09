A = [1, 2, 3]

n, mod = len(A), 10**9 + 7
left_min, right_min, left_max, right_max = [0] * n, [0] * n, [0] * n, [0] * n

s1, s2 = [], []

for i, num in enumerate(A):
    count = 1
    while s1 and s1[-1][0] > num:
        count += s1.pop()[1]
    left_min[i] = count
    s1.append([num, count])

    count = 1
    while s2 and s2[-1][0] < num:
        count += s2.pop()[1]
    left_max[i] = count
    s2.append([num, count])

s1, s2 = [], []
for i, num in list(enumerate(A))[::-1]:
    count = 1
    while s1 and s1[-1][0] > num:
        count += s1.pop()[1]
    right_min[i] = count
    s1.append([num, count])

    count = 1
    while s2 and s2[-1][0] < num:
        count += s2.pop()[1]
    right_max[i] = count
    s2.append([num, count])

cn = [1, 2, 33, 34, 3434, 3434, 3434343,
      3434, 434]

print(sum(an * l * r for an, l, r in zip(A, left_min, right_min)))
print(sum(an * l * r for an, l, r in zip(A, left_max, right_max)))
