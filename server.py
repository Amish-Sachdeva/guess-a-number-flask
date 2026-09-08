from flask import Flask
from random import randint
random_no = randint(0, 9)
app = Flask(__name__)

@app.route('/')
def home():
    return f"<h1> Guess a number between 0 and 9 </h1>" \
            '<img src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif" />'

@app.route('/<int:guess>')
def guess_number(guess):
    if random_no > guess:
        return '<h1>Too Low, Try again!</h1>' \
                '<img src="https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif" />'
    elif random_no < guess:
        return '<h1>Too high, Try again!</h1>' \
                '<img src="https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif" />'

    elif random_no == guess:
        return '<h1>You found me!</h1>' \
                '<img src="https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif" />'

if __name__ == '__main__':
    app.run()
