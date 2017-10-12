from guizero import App, Slider, TextBox, Box
import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)

GPIO.setmode(GPIO.BCM)
GPIO.setup(20, GPIO.OUT)
GPIO.setup(21, GPIO.OUT)
GPIO.setup(22, GPIO.OUT)

RED = GPIO.PWM(20, 100)
RED.start(100)
GREEN = GPIO.PWM(21, 100)
GREEN.start(100)
BLUE = GPIO.PWM(22, 100)
BLUE.start(100)

red1 = 0
green1 = 0
blue1 = 0

def red_slider_changed(red_value):
    global red1
    red1 = red_value
    app.bgcolor('#%02x%02x%02x' % (int(red1)*2.55, int(green1)*2.55, int(blue1)*2.55))
    RED.ChangeDutyCycle(100-float(red1))


def green_slider_changed(green_value):
    global green1
    green1 = green_value
    app.bgcolor('#%02x%02x%02x' % (int(red1)*2.55, int(green1)*2.55, int(blue1)*2.55))
    GREEN.ChangeDutyCycle(100-float(green1))

def blue_slider_changed(blue_value):
    global blue1
    blue1 = blue_value
    app.bgcolor('#%02x%02x%02x' % (int(red1)*2.55, int(green1)*2.55, int(blue1)*2.55))
    BLUE.ChangeDutyCycle(100-float(blue1))

app = App(bgcolor = "white")

red = Slider(app, command=red_slider_changed, start=0, end=100)
green = Slider(app, command=green_slider_changed, start=0, end=100)
blue = Slider(app, command=blue_slider_changed, start=0, end=100)
