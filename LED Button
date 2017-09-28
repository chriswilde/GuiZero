from guizero import App, PushButton
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setup(3, GPIO.OUT)
GPIO.output(3, GPIO.LOW)

def light_switch():

  if GPIO.input(3):
    GPIO.output(3, GPIO.LOW)
    LED_Control["text"] = "SWITCH LED ON"
    print("LED is now off")
  else:
    GPIO.output(3, GPIO.HIGH)
    LED_Control["text"] = "SWITCH LED OFF"
    print("LED is now on")
    
 app = App(title = "LED Play")
 LED_Control = PushButton(app, command = light_Switch, text = "SWITCH LED ON")
 app.display()
