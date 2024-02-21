from math import sqrt

def is_prime(n):
    i = 2
    while i <= sqrt(n):
        if n % i == 0:
            return 0
        i+=1
    return 1

def div_list(n):
    i=2
    list = []
    while i<=sqrt(n):
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


print(fi(63))