from guizero import App, Box, Text

app = App(title="My app", height=300, width=200)
box = Box(app)

boxText = Text(box, text="Hello from the box", size=14, color="red", font="Arial")
appText = Text(app, text="Hello from the app", size=14, color="blue", font="Courier New")

app.display()
