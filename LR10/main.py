import random
import sympy

def generate_keypair(bits=64):
    # Генерация двух простых чисел p и q
    p = sympy.randprime(2**(bits//2), 2**(bits//2 + 1))
    q = sympy.randprime(2**(bits//2), 2**(bits//2 + 1))

    # Вычисление модуля n и открытой экспоненты e
    n = p * q
    phi_n = (p - 1) * (q - 1)
    e = 65537  # Обычно выбирается стандартное значение

    # Вычисление закрытой экспоненты d
    d = sympy.mod_inverse(e, phi_n)

    public_key = (n, e)
    private_key = (n, d)

    return public_key, private_key

def encrypt(message, public_key):
    n, e = public_key
    # Преобразование сообщения в число
    m = int.from_bytes(message.encode(), byteorder='big')
    # Шифрование: c = m^e mod n
    c = pow(m, e, n)
    return c

def decrypt(ciphertext, private_key):
    n, d = private_key
    # Расшифрование: m = c^d mod n
    m = pow(ciphertext, d, n)
    # Преобразование числа обратно в строку
    message = m.to_bytes((m.bit_length() + 7) // 8, byteorder='big').decode()
    return message

def save_private_key(private_key, filename='private_key.txt'):
    with open(filename, 'w') as f:
        f.write(','.join(str(x) for x in private_key))

def load_private_key(filename='private_key.txt'):
    with open(filename, 'r') as f:
        private_key = tuple(int(x) for x in f.read().split(','))
    return private_key

def save_public_key(public_key, filename='public_key.txt'):
    with open(filename, 'w') as f:
        f.write(','.join(str(x) for x in public_key))

def load_public_key(filename='public_key.txt'):
    with open(filename, 'r') as f:
        public_key = tuple(int(x) for x in f.read().split(','))
    return public_key

if __name__ == "__main__":
    # Генерация ключевой пары
    public_key, private_key = generate_keypair()

    # Сохранение закрытого ключа в файл
    save_private_key(private_key)

    # Сохранение открытого ключа в файл
    save_public_key(public_key)

    # Показ открытого ключа пользователю
    print("Открытый ключ (n, e):", public_key)

    # Шифрование сообщения
    message = input("Введите сообщение для шифрования: ")
    ciphertext = encrypt(message, public_key)
    print("Зашифрованное сообщение:", ciphertext)

    # Расшифрование сообщения
    loaded_private_key = load_private_key()
    decrypted_message = decrypt(ciphertext, loaded_private_key)
    print("Расшифрованное сообщение:", decrypted_message)
