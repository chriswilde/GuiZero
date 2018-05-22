from guizero import App, Text, Box, PushButton
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(2, GPIO.OUT)
GPIO.output(2, GPIO.LOW)

def do_nothing():
  print("Nothing Happened")
  GPIO.output(2, GPIO.HIGH)
  time.sleep(2)
  GPIO.output(2, GPIO.LOW)
  
    
app = App(title="Keypad Example", height=100, width=90, layout="grid")

button1 = PushButton(box, command=do_nothing, text="LED 1", grid=[0,0])
button2 = PushButton(box, command=do_nothing, text="LED 2", grid=[0,1])
button3 = PushButton(box, command=do_nothing, text="LED 3", grid=[0,2])
button4 = PushButton(box, command=do_nothing, text="LED 4", grid=[1,0])
button5 = PushButton(box, command=do_nothing, text="LED 5", grid=[1,1])
button6 = PushButton(box, command=do_nothing, text="LED 6", grid=[1,2])

app.display(
