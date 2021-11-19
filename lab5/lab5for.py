n = int(input('Введіть n: '))

max_sum = 0
max_number = 0
for j in range(1, n + 1):
    s = 0
    for i in range(1, j+1):
        if j % i == 0:
            s += i

        if max_sum < s:
            max_sum = s
            max_number = j

print(f'Максимальне число: {max_number}')
print(f'Максимальна сума: {max_sum}')

