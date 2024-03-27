import random
import math

def is_prime_AKS(n):
    # Проверка, является ли число 2 или 3
    if n == 2 or n == 3:
        return True

    # Проверка, кратно ли число 2 или 3
    if n % 2 == 0 or n % 3 == 0:
        return False

    # Вычисление k, такого что n = 2^r * d + 1, где d нечетное
    r, d = 0, n - 1
    while d % 2 == 0:
        r += 1
        d //= 2

    # Проверка простоты для нескольких случайных значений a
    for _ in range(5):  # можно увеличить количество итераций для большей уверенности
        a = random.randint(2, n - 2)
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False

    return True

def is_prime_standard(n):
    # Проверка всех чисел от 2 до корня из n
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def save_primes(filename, primes):
    with open(filename, 'w') as f:
        for prime in primes:
            f.write(str(prime) + '\n')

if __name__ == "__main__":
    # Поиск всех простых чисел до 1000000 с помощью AKS и стандартного метода
    aks_primes = [n for n in range(2, 1000000) if is_prime_AKS(n)]
    standard_primes = [n for n in range(2, 1000000) if is_prime_standard(n)]

    # Сравнение результатов двух методов
    print("Количество простых чисел до 1000000 по AKS:", len(aks_primes))
    print("Количество простых чисел до 1000000 по стандартному методу:", len(standard_primes))
    print("Результаты совпадают:", aks_primes == standard_primes)

    # Запись всех простых чисел до 1000000 в файл
    save_primes("primes.txt", aks_primes)
