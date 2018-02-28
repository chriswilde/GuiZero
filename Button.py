from guizero import App, TextBox
from gpiozero import Button
import time

input = Button(21)

def display():
  name.clear()
  name.set("BOOOOOOM!!!!")
  app.bgcolor("black")
  
input.when_pressed = display

app = App(bgcolor = "pink")
name = textBox(app, text = "Not Pressed")
app.display()
