from math import sqrt

def evkl(a,b):
    if b == 0:
        return a, 1, 0
    else:
        gcd, x1, y1 = evkl(b, a%b)
    x = y1
    y = x1 - (a//b) * y1
    return gcd, x, y

def div_list(n):
    i=2
    list = []
    while i <= n/2:
        if is_prime(i) and n%i==0:
            list.append(i)
        i+=1
    return list

def fi(n):
    if is_prime(n):
        return n-1
    p=n
    l=div_list(n)
    for i in range(len(l)):
        p*=1-(1/l[i])
    return int(p)

def is_prime(n):
    i = 2
    while i <= sqrt(n):
        if n % i == 0:
            return 0
        i+=1
    return 1


class ModularExponentiation:
    def __init__(self, modulus):
        self.modulus = modulus

    def _modular_multiply(self, a, b):
        return ( (a % self.modulus) * (b % self.modulus) ) % self.modulus

    def _modular_add(self, a, b):
        return ( (a % self.modulus) + (b % self.modulus) ) % self.modulus


    def ost(self, n):
        k = fi(self.modulus)
        return n%k

    def positive_exponentiation(self, number, exp):
        return (number**self.ost(exp)) % self.modulus

    def negative_exponentiation(self, number, exp):
        return self.positive_exponentiation(evkl(number, self.modulus)[1], abs(exp))



# Пример использования
mod_exp = ModularExponentiation(10)  # Заданный модуль

# Вычисление положительной степени
print("7**47 \u2261 " + str(mod_exp.positive_exponentiation(7,43)) + " mod " + str(mod_exp.modulus))

mod_exp2 = ModularExponentiation(7)

print("3**28 \u2261 " + str(mod_exp2.positive_exponentiation(3,28)) + " mod " + str(mod_exp2.modulus))
print(ModularExponentiation(78).negative_exponentiation(17, -2))

# надо возводить в степень как в тетрадке
# находить обратный элемент методом сравнения