from flask import Flask
import random

app = Flask(__name__)
r_number = random.randint(1, 9)

@app.route('/')
def home():
    return '<h1 align = "center">Guess a number between 0 and 9 </h1>' \
           '<img src="https://giphy.com/gifs/CoinsAndConnections-illustration-typography-question-Rs2QPsshsFI9zeT4Kn" width="500" height="600"></img>'

@app.route("/<int:guess>")
def guess_number(guess):
    if r_number == guess:
        return '<img src="https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif" height="600"></img>'\
               '<h1 align = "center"> Correct </h1>'
    elif r_number > guess:
        return '<img src="https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif" height="600"></img>'\
                '<h1 align = "center">Hight</h1>'
    elif r_number < guess:
        return '<img src="https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif" height="600"></img>' \
               '<h1 align = "center">Less</h1>'

app.run()
