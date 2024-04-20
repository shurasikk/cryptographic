from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import ec

#Схема Шнорра

def generate_key_pair():
    # выбираем простое число p
    # выбираем число q чтобы оно было делителем p-1

    private_key = ec.generate_private_key(ec.SECP256R1(), default_backend()) #параметр кривой
    public_key = private_key.public_key()
    return private_key, public_key


def sign_message(private_key, message):
    hash_value = hashes.Hash(hashes.SHA256(), default_backend())
    hash_value.update(message.encode())
    digest = hash_value.finalize()

    signature = private_key.sign(digest, ec.ECDSA(hashes.SHA256()))
    return signature


def verify_signature(public_key, signature, message):
    hash_value = hashes.Hash(hashes.SHA256(), default_backend())
    hash_value.update(message.encode())
    digest = hash_value.finalize()

    try:
        public_key.verify(signature, digest, ec.ECDSA(hashes.SHA256()))
        return True
    except Exception:
        return False


# Пример использования:

# Генерация ключевой пары
private_key, public_key = generate_key_pair()

# Сообщение для подписи
message = "Hello, world!"

# Подпись сообщения
signature = sign_message(private_key, message)

# Вывод подписи
print("Signature:", signature.hex())

# Проверка подписи
is_valid = verify_signature(public_key, signature, message)
if is_valid:
    print("Signature is valid.")
else:
    print("Signature is not valid.")
