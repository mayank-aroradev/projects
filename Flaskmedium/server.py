from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("low.html")

if __name__ == "__main__":
    app.run(debug=True)

# html file can be rendered into flask 
# imgs and other files which are static will be in static file 
# where as html willl be in templates
