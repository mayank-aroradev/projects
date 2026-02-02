from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "<h2>Hello, daddy!</h2>"
@app.route("/username/<name>")
def greet(name):
    return f"hello {name}!"

@app.route("/username/<name>/<int:number>")
def greetme(name,number):
    return "Hello there {name},your age is {number} year old!"
if __name__ == "__main__":
    app.run(debug=True)
    