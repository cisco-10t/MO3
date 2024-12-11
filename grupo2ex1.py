def LetrasIguais(texto):
    for letra in texto:
        if letra !=texto[0]:
            return False
    return True