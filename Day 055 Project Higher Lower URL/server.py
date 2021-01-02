from flask import Flask
import random

app = Flask(__name__)

HOME_GIF_URL = 'https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif'
NUMBER_HIGH_GIF_URL = 'https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif'
NUMBER_LOW_GIF_URL = 'https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif'
NUMBER_FOUND_GIF_URL = 'https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif'


# def make_bold(function):
#     def bold():
#         return f'<b>{function()}</b>'
#
#     return bold
#
#
# def make_emphasis(function):
#     def emphasis():
#         return f'<em>{function()}</em>'
#
#     return emphasis
#
#
# def make_underlined(function):
#     def underline():
#         return f'<u>{function()}</u>'
#
#     return underline


@app.route('/')
def home():
    return f'<h1>Guess a number between 0 and 9</h1>' \
           f'<img src={HOME_GIF_URL}>'


@app.route('/<int:num>')
def guess_page(num):
    if num < random_num:
        return '<h1 style="color:red;">Number too low</h1>' \
               f'<img src={NUMBER_LOW_GIF_URL}>'
    elif num > random_num:
        return '<h1 style="color:blue;">Number too High</h1>' \
               f'<img src={NUMBER_HIGH_GIF_URL}>'
    else:
        return '<h1 style="color:green;">Number Found!</h1>' \
               f'<img src={NUMBER_FOUND_GIF_URL}>'


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    random_num = random.randint(1, 9)
    app.run(debug=True)
