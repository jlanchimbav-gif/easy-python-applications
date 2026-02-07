## Aplicacion de Alarma Simple en Python ##

import time
from datetime import datetime
import os

def set_alarm(alarm_time):
	"""Set an alarm for a specific time (HH:MM format)"""
	while True:
		current_time = datetime.now().strftime("%H:%M")
		if current_time == alarm_time:
			print("¡Alarma! La hora ha llegado.")
			break
		time.sleep(1)

if __name__ == "__main__":
	alarm_time = input("Ingresa la hora de la alarma (HH:MM): ")
	set_alarm(alarm_time)

    # Optional: Add a sound alert
    if os.name == 'nt':  # Windows
        os.system('powershell -c "(New-Object System.Media.SoundPlayer "C:\\Windows\\Media\\alarm.wav").PlaySync()"')
    else:  # Linux/Mac
        os.system('afplay /System/Library/Sounds/Alarm.aiff')