#Q10.Write a code to trigger alarm for you at scheduled time.

import datetime
from playsound import playsound
Alarm_Hour = int(input("Enter Hour: "))
Alarm_Minute = int(input("Enter Minute: "))
AmPm = str(input("Enter Am or Pm: "))
if AmPm == "pm":
    Alarm_Hour = Alarm_Hour + 12
while True:
    if Alarm_Hour == datetime.datetime.now().hour and Alarm_Minute == datetime.datetime.now().minute:
        print("Playing...")
        playsound("mixkit-alarm-digital-clock-beep-989.wav")
        break

