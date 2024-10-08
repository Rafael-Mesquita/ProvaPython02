def is_palindrome(s):
    s = s.lower().replace(" ", "").replace(",", "").replace(".", "")
    return s == s[::-1]

entrada = input("Digite uma palavra ou frase: ")
if is_palindrome(entrada):
    print("É um palíndromo.")
else:
    print("Não é um palíndromo.")
