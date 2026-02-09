from flask import Flask,render_template
import random
import requests
import datetime
app = Flask(__name__)
@app.route("/")
def call():
    we=random.randint(1,10)
    y= datetime.datetime.now().year
    return render_template("index.html",num=we, year=y)
@app.route("/<name>") 
def greet(name):
    gender_url=f"https://api.genderize.io?name={name}"
    gender_respo=requests.get(gender_url)
    gender_data=gender_respo.json()
    gender=gender_data["gender"]
    age_url=f"https://api.agify.io?name={name}"
    age_respo=requests.get(age_url)
    age_data=age_respo.json()
    age=age_data["age"]
    return render_template("api.html",name=name,gender=gender,age=age)

@app.route("/blog")
def blog():
    blog_url="https://api.npoint.io/c790b4d5cab58020d391"
    blog_respo=requests.get("https://api.npoint.io/c790b4d5cab58020d391")
    blog_data=blog_respo.json()


    return render_template("blog.html",blog_data=blog_data)

if __name__=="__main__":
    app.run(debug=True)
