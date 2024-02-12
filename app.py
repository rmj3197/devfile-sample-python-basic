from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def hello():
    print("Hello World")
    return "Hello World!"

if __name__ == '__main__':
    app.run()
