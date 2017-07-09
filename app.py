from LED import LED
from flask import Flask
from flask import render_template, request, redirect, url_for
import _thread

app = Flask(__name__)
lights = LED(255, 102, 0, 1)
lights.gpio()


@app.route('/')
@app.route('/<int:power>')
@app.route('/<int:red>,<int:green>,<int:blue>')
@app.route('/<int:red>,<int:green>,<int:blue>,<int:power>')
def index(red=None, green=None, blue=None, power=None, function=None):
    lights.fading = False
    # only update color if a color is specified and max is 255
    if red is None:
        red = lights.red

    if green is None:
        green = lights.green

    if blue is None:
        blue = lights.blue

    if power is None:
        power = lights.power
    elif power > 1 and power <= 100:
        power /= 100
    elif power > 100:
        power = 1

    lights.update(red, green, blue, power)

    if power == 0:
        print("powering off")
        lights.off()
    else:
        pass
        lights.gpio()

    return render_template('index.html', lights=lights)

@app.route('/', methods=['POST'])
def post():
    red = request.form['red']
    green = request.form['green']
    blue = request.form['blue']
    lights.update(red, green, blue, 1)
    return redirect(url_for('index'))


@app.route('/fade<int:speed>')
@app.route('/fade<int:red>,<int:green>,<int:blue>')
@app.route('/fade<int:red>,<int:green>,<int:blue>,<int:speed>')
def fade(red=None, green=None, blue=None, speed=0):
    if red is None:
        red = lights.red
    elif red > 255:
        red = 255

    if green is None:
        green = lights.green
    elif green > 255:
        green = 255

    if blue is None:
        blue = lights.blue
    elif blue > 255:
        blue = 255

    if speed is not 0 and lights.fading:
        lights.speed = speed
        return ('', 204)
    else:
        _thread.start_new_thread(lights.fade, (red, green, blue))

    return render_template('fading.html', lights=lights, r=red, g=green, b=blue)
