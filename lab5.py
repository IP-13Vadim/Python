from math import sqrt


def sdiv(n):
    sum = 0

    for i in range(1, round(n/2)):
        if n % i == 0:
            sum += i + (n / i)

    i = round(sqrt(n))

    if i*i == n:
        sum += i

    return sum


if __name__ == '__main__':
    n = int(input('Введіть n: '))

    max_sum = 0
    max_number = 0

    for j in range(1, n+1):
        s = sdiv(j)
        if max_sum < s:
            max_sum = s
            max_number = j

    print(f'Максимальне число: {max_number}')
    print(f'Максимальна сума: {max_sum}')