import datetime
#data de hoje
print(datetime.date.today())

#ano
print(datetime.date.today().year)
#mes
print(datetime.date.today().month)
#dia
print(datetime.date.today().day)
#data e hora
print(datetime.datetime.now())
#com string
print(datetime.datetime.now().strftime("%d - %m - %Y - %H:%M:%S"))