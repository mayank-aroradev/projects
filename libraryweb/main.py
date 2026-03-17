from flask import Flask, render_template, request, redirect, url_for
from flask_bootstrap import Bootstrap
import sqlite3
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField,URLField,SelectField
import os
from wtforms.validators import DataRequired,URL



class add(FlaskForm):
    Name=StringField("NAME OF THE BOOK", validators=[DataRequired()])
    BOOK=StringField("AUTHOR OF THE BOOK", validators=[DataRequired()])
    RATE=StringField("RATING", validators=[DataRequired()])
    submit=SubmitField("SUBMIT")
app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7CsKR6b'
all_books = []


@app.route('/')
def home():
    return render_template("index.html",books=all_books)
    pass



@app.route("/add",methods=["GET", "POST"])
def addme():
    form=add()
    
    if form.validate_on_submit():
        new_book={
            "title":form.Name.data,
            "author":form.BOOK.data,
            "rating": form.RATE.data }
        all_books.append(new_book)
        return redirect(url_for('home'))
    return render_template("add.html",form=form)
    pass


if __name__ == "__main__":
    app.run(debug=True)

