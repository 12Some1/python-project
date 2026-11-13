def g_senha(comprimento):
    letras = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
    senha = ""
    import random as r
    for _ in range(comprimento):
        senha += letras[r.randint(0, len(letras) - 1)]
    return senha
