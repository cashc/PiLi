from LED import LED
from flask import Flask
from flask import render_template

app = Flask(__name__)
lights = LED(5, 30, 15, .3)
lights.gpio()

@app.route('/')
@app.route('/<int:power>')
@app.route('/<int:red>,<int:green>,<int:blue>')
@app.route('/<int:red>,<int:green>,<int:blue>,<int:power>')
def index(red=None, green=None, blue=None, power=None):
    # only update color if a color is specified and max is 255
    if red is None: red = lights.red
    elif red>255: red=255

    if green is None: green = lights.green
    elif green>255: green=255

    if blue is None: blue = lights.blue
    elif blue>255: blue=255

    if power is None: power = lights.power
    elif power>1 and power<=100: power/=100
    else: power = 1

    lights.update(red, green, blue, power)

    if power == 0:
        print("powering off")
        lights.off()
    else:
        lights.gpio()

    return render_template('index.html', lights=lights)
