f = [0, 1, 1]
n = 10
print('*' * 100)
print(f[2])

for i in range(3, n + 1):
    f.append(f[i - 1] + f[i - 2])
    # f[i] = f[i - 1] + f[i - 2]

print('=' * 100)
print(f)
# i = 3
# while (i <= n):
#     f.append()
