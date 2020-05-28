from flask import Flask
from vsearch import search4letters

# print(__name__)
app = Flask(__name__)

@app.route('/')
def hello() -> str:
    return 'Hello world from Flask!'

@app.route('/search4')
def do_search() -> str:
    return str(search4letters('life, the universe, and everthing', 'eiru'))

app.run()