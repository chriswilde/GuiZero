from guizero import App, Text, Box, PushButton
def do_nothing():
    return 0

app = App(title="My app", height=300, width=200, layout="grid")
text = Text(app, text="There is a grid here", grid=[0,0])

box = Box(app, layout="grid", grid=[0,1])

button1 = PushButton(box, command=do_nothing, text="1", grid=[0,0])
button2 = PushButton(box, command=do_nothing, text="2", grid=[0,1])
button3 = PushButton(box, command=do_nothing, text="3", grid=[0,2])
button4 = PushButton(box, command=do_nothing, text="4", grid=[1,0])
button5 = PushButton(box, command=do_nothing, text="5", grid=[1,1])
button6 = PushButton(box, command=do_nothing, text="6", grid=[1,2])

app.display()
