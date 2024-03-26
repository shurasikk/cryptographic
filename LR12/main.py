from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import ec


# Генерация ключей
def generate_key_pair():
    private_key = ec.generate_private_key(ec.SECP256R1(), default_backend())
    public_key = private_key.public_key()
    return private_key, public_key


# Подписание сообщения
def sign_message(private_key, message):
    signature = private_key.sign(
        message,
        ec.ECDSA(hashes.SHA256())
    )
    return signature


# Проверка подписи
def verify_signature(public_key, signature, message):
    try:
        public_key.verify(
            signature,
            message,
            ec.ECDSA(hashes.SHA256())
        )
        print("Подпись верна.")
    except:
        print("Ошибка проверки подписи.")


# Пример использования
if __name__ == "__main__":
    private_key, public_key = generate_key_pair()
    message = b"Message"

    signature = sign_message(private_key, message)
    print("Подпись:", signature.hex())

    verify_signature(public_key, signature, message)
