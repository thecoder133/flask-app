from flask import Flask, render_template
import random
app = Flask(__name__)

@app.route('/')
def hello_world():
    num = random.randint(0, 99)
    return render_template('index.html', num=num)
