import datetime

dia=int(input("Dia de nascimento: "))
mes=int(input("Mes de nascimneto: "))
ano=int(input("Ano de nascimento: "))

hoje=datetime.date.today()

data_nascimento=datetime.date(ano,mes,dia)

idade=hoje.year - data_nascimento.year
if data_nascimento.month> hoje.month or (data_nascimento.month==hoje.month and data_nascimento.day):
    idade-=1
print(idade)