import random
import sympy

def generate_keypair(bits=64):
    p = sympy.randprime(2**(bits//2), 2**(bits//2 + 1))
    q = sympy.randprime(2**(bits//2), 2**(bits//2 + 1))
    n = p * q
    phi_n = (p - 1) * (q - 1)
    e = 65537
    d = sympy.mod_inverse(e, phi_n)
    public_key = (n, e)
    private_key = (n, d, p, q)
    return public_key, private_key

def encrypt(message, public_key):
    n, e = public_key
    m = int.from_bytes(message.encode(), byteorder='big')
    c = pow(m, e, n)
    return c

def decrypt(ciphertext, private_key):
    n, d, _, _ = private_key
    m = pow(ciphertext, d, n)
    message = m.to_bytes((m.bit_length() + 7) // 8, byteorder='big').decode()
    return message

def save_private_key(private_key, filename='private_key.txt'):
    with open(filename, 'w') as f:
        f.write(','.join(str(x) for x in private_key))

def save_public_key(public_key, filename='public_key.txt'):
    with open(filename, 'w') as f:
        f.write(','.join(str(x) for x in public_key))

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
    decrypted_message = decrypt(ciphertext, private_key)
    print("Расшифрованное сообщение:", decrypted_message)
