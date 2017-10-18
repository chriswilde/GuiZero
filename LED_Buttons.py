from guizero import App, PushButton
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(3, GPIO.OUT)
GPIO.output(3, GPIO.LOW)

def light_Switch():
  GPIO.output(3, GPIO.HIGH)
  time.sleep(2)
  GPIO.output(3, GPIO.LOW)
  
    
 app = App(title = "LED Play")
 LED_Control = PushButton(app, command = light_Switch, text = "SWITCH LED ON")
 app.display()
