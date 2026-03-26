from flask import Flask, render_template, redirect, url_for,request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Text,ForeignKey
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, URL
from flask_ckeditor import CKEditor, CKEditorField
from datetime import date
import os
from forms import registerform,loginform,commentform
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user
from werkzeug.security import generate_password_hash, check_password_hash
from functools  import wraps
from flask import abort 

def admin_only(f):
    @wraps(f)
    def decorated_function(*args,**kwargs):
        if current_user.id != 1:
            return abort(403)
        return f(*args,**kwargs)
    return decorated_function

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__, instance_path=os.path.join(basedir, 'instance'))

login_manager=LoginManager()
login_manager.init_app(app)
@login_manager.user_loader
def load_user(user_id):
    return db.get_or_404(User,user_id)

app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)
ckeditor = CKEditor(app)
# CREATE DATABASE
class Base(DeclarativeBase):
    pass
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)


# CONFIGURE TABLE
class BlogPost(db.Model):
    __tablename__="blog_posts"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    author_id:Mapped[int]=mapped_column(ForeignKey("users.id"))
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    subtitle: Mapped[str] = mapped_column(String(250), nullable=False)
    date: Mapped[str] = mapped_column(String(250), nullable=False)
    body: Mapped[str] = mapped_column(Text, nullable=False)
    author: Mapped[str] = mapped_column(String(250), nullable=False)
    img_url: Mapped[str] = mapped_column(String(250), nullable=False)

class User(UserMixin,db.Model):
    __tablename__="users"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    email:Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    password:Mapped[str]= mapped_column(String(250),unique=True,nullable=False)
    name: Mapped[str] = mapped_column(String(100))
class Comment(db.model):
    __tablename__="comments"
    id:Mapped[int] = mapped_column(Integer,primary_key=True)
    text:Mapped[str]=mapped_column(Text,nullable=False)
def get_dict(self):
    return{column.name:getattr(self,column.name) for column in self.__table__.columns}


with app.app_context():
    db.create_all()

class formpost(FlaskForm):
    title = StringField("Blog Post Title", validators=[DataRequired()])
    subtitle = StringField("Subtitle", validators=[DataRequired()])
    author = StringField("Your Name", validators=[DataRequired()])
    img_url = StringField("Blog Image URL", validators=[DataRequired(), URL()])
    # Notice body is using a CKEditorField and not a StringField
    body = CKEditorField("Blog Content", validators=[DataRequired()])
    submit = SubmitField("Submit Post")
@app.route('/')
def get_all_posts():
    result=db.session.execute(db.select(BlogPost))
    all_post=result.scalars().all()

    # TODO: Query the database for all the posts. Convert the data to a python list.
    # posts = [post.get_dict for post in all_post]
    # print(posts)
    return render_template("index.html", all_posts=all_post)

# TODO: Add a route so that you can click on individual posts.
@app.route('/post/<post_id>')
def show_post(post_id):
    result2=db.session.get(BlogPost,post_id)
    comment_form=commentform()

    return render_template("post.html", post=result2,form=comment_form)
from datetime import date
# TODO: add_new_post() to create a new blog post
@app.route('/new-post',methods=["GET","POST"])
@admin_only
def addpost():
    form=formpost()
    if form.validate_on_submit():
        new_post=BlogPost(
            title=form.title.data,
            subtitle=form.subtitle.data,
            body=form.body.data,
            img_url=form.img_url.data,
            author=form.author.data,
            date=date.today().strftime("%B %d, %Y")
        )
        db.session.add(new_post)
        db.session.commit()
        return redirect(url_for("get_all_posts"))
    return render_template('make-post.html',form=form)
# TODO: edit_post() to change an existing blog post
@app.route("/edit-post/<post_id>",methods=["GET","POST"])
def editit(post_id):
    post=db.get_or_404(BlogPost,post_id)
    edit_form=formpost(
        title=post.title,
        subtitle=post.subtitle,
        img_url=post.img_url,
        author=post.author,
        body=post.body
    )
    if edit_form.validate_on_submit():
        
            post.title = edit_form.title.data
            post.subtitle = edit_form.subtitle.data
            post.img_url = edit_form.img_url.data
            post.author = edit_form.author.data
            post.body = edit_form.body.data    
            db.session.commit()
            return redirect(url_for("show_post", post_id=post.id))
    return render_template("make-post.html",form=edit_form,is_edit=True)
# TODO: delete_post() to remove a blog post from the database
@app.route("/delete-post/<post_id>",methods=["GET","POST"])
@admin_only
def delete_post(post_id):
    result=db.get_or_404(BlogPost,post_id)
    db.session.delete(result)
    db.session.commit()
    return redirect(url_for('get_all_posts'))

# Below is the code from previous lessons. No changes needed.
@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")



@app.route("/register",methods=["GET","POST"])
def registeruser():
    form=registerform()
    if form.validate_on_submit():
        hashed_password=generate_password_hash(request.form.get('password'),
                                             method='pbkdf2:sha256',
                                            salt_length=8)
        new_user=User(
            email=form.email.data,
            name=form.name.data,
            password=hashed_password
        )
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for("get_all_posts"))
    return render_template("register.html", form=form)
        

@app.route("/login",methods=["GET","POST"])
def login():
    form=loginform()
    if form.validate_on_submit():
        email=form.email.data
        password=form.password.data
        result=db.session.execute(db.select(User).where(User.email==email))
        user=result.scalar()

        if user and check_password_hash(user.password,password):
            login_user(user)
            return redirect (url_for('get_all_posts'))
        
    return render_template('login.html',form=form)


if __name__ == "__main__":
    app.run(debug=True, port=5003)
