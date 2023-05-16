from flask import Flask
import random

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/<int:name>")
def greet(name):
    b = random.randint(1,10)
    if name < b:
        return f"{name} is less"
    elif name > b:
        return f"{name} is more"
    else:
        return f"{name} is equal"

if __name__ == '__main__':
    app.run(debug=True)
