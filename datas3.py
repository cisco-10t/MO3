from datetime import datetime
import time
despertou=False

while True:
    hora_atual=datetime.now(),strftime("%H:%M:%s")
    print(hora_atual)
    time.sleep(1)
    if datetime.now().hour>=16 and datetime.now().minute>=35 and datetime.now().second>=0 and despertou==False:
        print("ACORDAAAA!!!!!!!!!!!")
        despertou=True