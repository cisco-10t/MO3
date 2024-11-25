def saudacao(texto="mundo"):
    print(f"olá, {texto}")
def saudacao2(nome, parte_dia="bom dia"):
    print(f"{parte_dia}, {nome}")
#saudacao()
#saudacao("Joaquim")
saudacao2(parte_dia="bom dia", nome="joaquim")
saudacao2(parte_dia="boa tarde", nome="maria")
saudacao2(nome="joaquim")