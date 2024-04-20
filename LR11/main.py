from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes


def devries_meyer_hash(message, key):
    block_size = len(key)
    num_blocks = (len(message) + block_size - 1) // block_size  # Количество блоков, округленное вверх
    message_padded = message.ljust(num_blocks * block_size, b'\x00')  # Дополнение нулями

    # Применение схемы Девиса-Мейера
    hash_result = bytearray(key)
    for i in range(num_blocks):
        block_start = i * block_size
        block_end = block_start + block_size
        block = message_padded[block_start:block_end]
        # XOR блока сообщения с текущим хешем
        for j in range(len(block)):
            hash_result[j] ^= block[j]

    return bytes(hash_result)


def hash_message(message, key):
    # Генерация случайного ключа, если не предоставлен
    if key is None:
        key = get_random_bytes(AES.block_size)
    # Построение хэша
    return devries_meyer_hash(message, key)


if __name__ == "__main__":
    # Пример использования
    message = b"Hello, world!"
    key = get_random_bytes(AES.block_size)  # Случайный ключ для блочного шифра
    cipher = AES.new(key, AES.MODE_ECB)  # Инициализация блочного шифра
    ciphertext = cipher.encrypt(message.ljust(len(message) + AES.block_size - (len(message) % AES.block_size),
                                              b'\x00'))  # Шифрование сообщения с дополнением
    hash_result = hash_message(ciphertext, key)  # Построение хэша от шифротекста
    print("Хэш:", hash_result.hex())
