def sum_div(num):
    sum = 0
    for i in range(1, num // 2 + 1):
        if num % i == 0:
            sum += i

    return sum


def init():
    n = int(input('n: '))
    return n


def solution(n):
    for i in range(1, n+1):
        a = sum_div(i)
        b = sum_div(a)

        if i == b and b != a:
            browse(i, a)


def browse(num1, num2):
    print(f'{num1}\t{num2}')


if __name__ == '__main__':
    solution(init())

