from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

def devide_meyer_hash(message, key):
    block_size = AES.block_size
    num_blocks = len(message) // block_size + 1
    message_padded = message.ljust(num_blocks * block_size, b'\x00')  # Дополнение нулями

    # Инициализация вектора инициализации (IV)
    iv = get_random_bytes(block_size)

    # Инициализация блочного шифра
    cipher = AES.new(key, AES.MODE_ECB)

    # Применение схемы Девиса-Мейера
    hash_result = iv
    for i in range(num_blocks):
        block_start = i * block_size
        block_end = block_start + block_size
        block = message_padded[block_start:block_end]
        # XOR блока сообщения с текущим хешем
        hash_result = bytes([a ^ b for a, b in zip(block, hash_result)])
        # Шифрование XOR'ированного блока
        hash_result = cipher.encrypt(hash_result)

    return hash_result

def hash_message(message, key):
    # Генерация случайного ключа, если не предоставлен
    if key is None:
        key = get_random_bytes(AES.block_size)
    # Построение хэша
    return devide_meyer_hash(message, key)

if __name__ == "__main__":
    # Пример использования
    message = b"Hello, world!"
    hash_result = hash_message(message, None)
    print("Хэш:", hash_result.hex())
