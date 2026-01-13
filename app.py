from flask import Flask, render_template
import random
app = Flask(__name__)

@app.route('/')
def main():
    return render_template('index.html')

@app.route('/num/<number>')
def num(number):
    num = random.randint(1, number)
    return f"Number between 1 and {number} is: {num}!"
