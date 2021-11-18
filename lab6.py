def sdiv(n, i=1):
    if i > n:
        return 0
    if n % i == 0:
        return i + sdiv(n, i+1) # <-- рекурсивний виклик методу
    return sdiv(n, i+1) # <-- рекурсивний виклик методу


if __name__ == '__main__':
    # Приймаємо введені дані з клавіатури і
    # приводимо їх до цільночисельного типу
    # та записуємо в змінну n
    n = int(input('Введіть n: '))

    max_sum = 0
    max_number = 0

    # Обчислюємо в циклі з межами [0; n] суми
    # множників числа на кожній ітерації
    #
    # range(1, n) => [0; n)
    # range(1, n+1) => [0; n]
    for j in range(1, n+1):
        s = sdiv(j)
        if max_sum < s:
            max_sum = s
            max_number = j

    print(f'Максимальне число: {max_number}')
    print(f'Максимальна сума: {max_sum}')