#programa para ler as notas de 3 alunos
from media import mediaD

nota1=int(input("Introduza uma nota: "))
nota2=int(input("Introduza uma nota: "))
nota3=int(input("Introduza uma nota: "))

media=mediaD(nota1,nota2,nota3)
print(f"A média das notas é de {media}")

