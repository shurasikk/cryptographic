from math import sqrt

def is_prime(n):
    i = 2
    while i <= sqrt(n):
        if n % i == 0:
            return 0
        i+=1
    return 1

def nod(a, b):
    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a
    return a

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

n = int(input("Введите число n, для которого найдём первообразные корни: "))

k = fi(fi(n))
l = div_list(fi(n))
print("1-й этап: Количество корней = " + str(k))

s = []
for i in range(len(l)):
    s.append(int(fi(n)/l[i]))

print("2-й этап: Будем возводить взаимно простые остатки в степени " + str(s))

cur = 0
i = 2
ans=[]
while i < n and cur<k:
    flag = 1
    print(str(i + 1) + "-й этап: ")
    if nod(n,i) == 1:
        for alph in range(len(s)):

            print(str(i) + "^^" + str(s[alph]) + " \u2261 " + str((i ** s[alph]) % n) + " mod " + str(n))

            if (i ** s[alph]) % n == 1:
                flag = 0
                print("Число не корень.")
                i+=1
                break
        if flag == 1:
            print("Число является корнем.")
            ans.append(i)
            cur+=1
            i+=1
    else:
        print("Число " + str(i) + " не является первообразным корнем, так как оно не взаимно простое с " + str(n))
        i+=1

print("Первообразными корнями являются числа " + str(ans))