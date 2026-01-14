from flask import Flask, render_template
import random
app = Flask(__name__)

@app.route('/')
def main():
    return render_template('index.html')

@app.route('/num')
def numnum():
    return "Add /y with y being any number you want to get a number between 1 and that number!!!"

@app.route('/num/<int:number>')
def num(number):
    num = random.randint(1, number)
    return f"Number between 1 and {number} is: {num}!"
@app.route('/liam')
def liam():
    return render_template('liam.html')

@app.route('/bored')
def bored():
    return "I AM BORED"

@app.route("/name/<str:name>")
def name(name):
    return f"Hello, {name.title()}!"