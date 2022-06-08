from flask import Flask
app = Flask(__name__)

@app.route('/')
def index2():
    return 'Hello world!!!'

@app.route('/pets')
def pets():
    return 'This is where we keep our pets info'

@app.route('/fruit/<int:f>')
def printFruit(f):
    print(f)
    return str(f)
