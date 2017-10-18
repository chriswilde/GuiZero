from guizero import App, PushButton
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(2, GPIO.OUT)
GPIO.output(2, GPIO.LOW)

def ledOne():
  GPIO.output(2, GPIO.HIGH)
  time.sleep(2)
  GPIO.output(2, GPIO.LOW)
  
def ledTwo():
  
def ledThree():
  
def ledFour():
  
def ledFive():
  
def ledSix():
  
    
app = App(title="Lots of LED's", height=300, width=200, layout="grid")
text = Text(app, text="There is a grid here", grid=[0,0])

box = Box(app, layout="grid", grid=[0,1])

button1 = PushButton(box, command=ledOne, text="LED 1", grid=[0,0])
button2 = PushButton(box, command=ledTwo, text="LED 2", grid=[0,1])
button3 = PushButton(box, command=ledThree, text="LED 3", grid=[0,2])
button4 = PushButton(box, command=ledFour, text="LED 4", grid=[1,0])
button5 = PushButton(box, command=ledFive, text="LED 5", grid=[1,1])
button6 = PushButton(box, command=ledSix, text="LED 6", grid=[1,2])

app.display()
