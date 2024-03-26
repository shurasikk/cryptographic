from sympy import Symbol, GF, gcd, div, expand


def create_gf_calculator(polynomial):
    x = Symbol('x')
    F = GF(2 ** len(polynomial))  # Поле Галуа GF(2^n) с заданным образующим многочленом
    GF_p = F.field


    # Определение образующего многочлена
    generator_poly = sum([poly * x ** exp for exp, poly in enumerate(reversed(polynomial))])

    def add(a, b):
        return GF_p((a + b) % 2)

    def multiply(a, b):
        return GF_p((a * b) % 2)

    def divide(a, b):
        quotient, remainder = div(a, b, domain=GF(2))
        return quotient

    def power(a, n):
        return expand(a ** n)

    def gcd_func(a, b):
        return gcd(a, b)

    def multiplication_table():
        table = [[None] * 256 for _ in range(256)]
        for i in range(256):
            for j in range(256):
                table[i][j] = multiply(i, j)
        return table

    return {
        'add': add,
        'multiply': multiply,
        'divide': divide,
        'power': power,
        'gcd': gcd_func,
        'multiplication_table': multiplication_table
    }



def main():
    print("Введите образующий многочлен (в виде списка коэффициентов):")
    polynomial_coefficients = list(map(int, input().split()))

    calculator = create_gf_calculator(polynomial_coefficients)

    while True:
        print("\nВыберите операцию:")
        print("1. Сложение")
        print("2. Умножение")
        print("3. Деление")
        print("4. Возведение в степень")
        print("5. НОД")
        print("6. Таблица умножения")
        print("7. Выход")

        choice = int(input("Введите номер операции: "))

        if choice == 7:
            print("Выход из программы.")
            break

        if choice == 6:
            table = calculator['multiplication_table']()
            for row in table:
                print(row)
            continue

        print("Введите два числа:")
        a = int(input())
        b = int(input())

        if choice == 1:
            result = calculator['add'](a, b)
        elif choice == 2:
            result = calculator['multiply'](a, b)
        elif choice == 3:
            result = calculator['divide'](a, b)
        elif choice == 4:
            n = int(input("Введите степень: "))
            result = calculator['power'](a, n)
        elif choice == 5:
            result = calculator['gcd'](a, b)

        print("Результат:", result)


if __name__ == "__main__":
    main()
