def verificar_primos(numeros):
    def is_prime(num):
        if num <= 1:
   return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    return [num for num in numeros if is_prime(num)]

numeros = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
primos = verificar_primos(numeros)
print(primos)