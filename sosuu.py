def sosuu(num):
    prime = True
    for i in range(2,num//2):
        if num % i == 0:
            prime = False
            print(i)
            break

    return prime
n = 5
print(sosuu(n))
