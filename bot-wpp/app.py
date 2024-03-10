import pywhatkit
import keyboard
import time
from datetime import datetime

contatos = ['+55xxxxxxxxxxx', '+55xxxxxxxxxx']

while len(contatos) >= 1:
    pywhatkit.sendwhatmsg(contatos[0],'teste do programa',datetime.now().hour,datetime.now().minute + 2)
    del contatos[1]
    time.sleep(60)
    keyboard.press_and_release('ctrl + w')
    
    
