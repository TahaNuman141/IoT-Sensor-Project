import random
import time
file=open("sensor_data.csv","a")
file.write("Tempearture,Humidity\n")
for i in range(10):
   

    temp=random.randint(35,67)
    hum=random.randint(45,80)
    print("Temperature",temp,"Humidity",hum)
    file.write(f"{temp},{hum}\n")
    file.flush()
    if temp>40:
        print("ALERT: HIGH TEMPERATURE! ")
        if hum>60:
         print("ALERT: HIGHT HUMIDITY!")

    time.sleep(2)
