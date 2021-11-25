n = 0


def sum_div(num):
    sum = 0

    # 1. Який проміжок буде обробляти цикл нижче?
    # 2. Для чого тут запис (num // 2 + 1)?
    # 3. Для чого використовується оператор // ?
    for i in range(1, num // 2 + 1):
        # 4. Для чого використовується оператор % ?
        if num % i == 0:
            sum += i

    return sum


def init():
    # 5. Для чого тут використовується ключове слово global?
    # (hint) https://codeguida.com/post/1381
    global n
    # 6. Для чого ми викликаємо метод int() ?
    n = int(input('n: '))


def solution():
    global n

    for i in range(1, n+1):
        a = sum_div(i)
        b = sum_div(a)

        if i == b and b != a:
            browse(i, a)


def browse(num1, num2):
    print(f'{num1}\t{num2}')


if __name__ == '__main__':
    init()
    solution()

