from flask import Flask , render_template,request
import requests
import smtplib
from post import Post
import datetime as dt
import os 
import smtplib
OWN_EMAIL=os.getenv('OWN_EMAIL')
OWN_PASSWORD=os.getenv('OWN_PASSWORD')
year=dt.datetime.now().year



posts=requests.get('https://api.npoint.io/7ebfc1ecf7fd58d61d8d').json()   
app= Flask(__name__)
@app.route("/")
def get_all_posts():
         
    return render_template("index.html",all_post=posts, yer=year)
@app.route("/aboutme")
def aboutme():
    return render_template("about.html", yer=year)
@app.route("/contactme")
def contactme():
    return render_template("contact.html", yer=year)
@app.route("/post/<int:index>")
def show_post(index):
    for blog_post in posts:
        if blog_post["id"] == index:
            return render_template("post.html", post=blog_post, yer=year)

@app.route("/datame" , methods=["GET","POST"])
def datame():
   
    if request.method=="POST":
        data = request.form
        user_name=(data["name"])
        user_email=(data["email"])
        user_number=(data["phone"])
        user_message=(data["message"])
        return render_template("success.html",)
        

        reciever_email=OWN_EMAIL
        password= OWN_PASSWORD
        message=f"Name:{user_name}\n Phone:{user_number}\nHELLO THERE\n{user_message}"
        msg = EmailMessage()
        msg.set_content(message)
        msg['subject']='you are the best'
        msg['from']=user_email
        msg['To']=recievers_email


        with smtplib.SMTP(host="smtp.gmail.com",port=587) as connection:
            connection.starttls()
            connection.login(receivers_email, password)
            connection.sendmail(OWN_EMAIL,OWN_EMAIL,email_message)
        return render_template("contact.html",msg_sent=True)
    return render_template('contact.html',msg_sent=False)



if __name__=="__main__":
    app.run(debug=True)