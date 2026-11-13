letras = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
comprimento = int(input("Digite o comprimento da senha: "))
senha = ""
import random as r
for _ in range(comprimento):
    senha += letras[r.randint(0, len(letras) - 1)]
print(senha)
