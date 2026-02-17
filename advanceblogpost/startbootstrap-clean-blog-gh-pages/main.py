from flask import Flask , render_template
import requests
from post import Post
import datetime as dt

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

@app.route("/contact" , methods=["POST"])
def datame():
    return 'success'



if __name__=="__main__":
    app.run(debug=True)