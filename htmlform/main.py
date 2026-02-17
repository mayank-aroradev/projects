from flask import Flask , render_template,request

app=Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')
@app.route("/login", methods=["POST"])
def login():
    username= request.form['username']
    password=request.form['password']
    return  f'<h1>Username:{username}</h1><h1>Password: {password}</h1>'




if __name__=="__main__":
    app.run(debug=True)

    # to get a hold of the html form method is used and in html we use action and method attribute 
    # https://www.w3schools.com/tags/att_form_method.asp
    # https://www.w3schools.com/tags/att_form_action.asp