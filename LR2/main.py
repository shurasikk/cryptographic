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

    def modular_multiply(self, a, b):
        return ( (a % self.modulus) * (b % self.modulus) ) % self.modulus

    def modular_add(self, a, b):
        return ( (a % self.modulus) + (b % self.modulus) ) % self.modulus


    def ost(self, n):
        k = fi(self.modulus)
        return n % k

    def positive_exponentiation(self, number, exp):
        if evkl(number, exp)[0] == 1:
            return (number**self.ost(exp)) % self.modulus

    def negative_exponentiation(self, number, exp):
        return self.positive_exponentiation(evkl(number, self.modulus)[1], abs(exp))

    def exponential(self, number, exp):
        if exp>0:
            return self.positive_exponentiation(number, exp)
        else:
            return self.negative_exponentiation(number, exp)


# Пример использования
mod_exp = ModularExponentiation(10)  # Заданный модуль

# Вычисление положительной степени
print("7**47 \u2261 " + str(mod_exp.positive_exponentiation(7,43)) + " mod " + str(mod_exp.modulus))

mod_exp2 = ModularExponentiation(3)

print("2**5 \u2261 " + str(mod_exp2.positive_exponentiation(2, 5)) + " mod " + str(mod_exp2.modulus))


# надо возводить в степень как в тетрадке
# находить обратный элемент методом сравнения