from flask import Flask, render_template, request, redirect, url_for


from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField,URLField,SelectField
import os
from wtforms.validators import DataRequired,URL
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float


app = Flask(__name__)

class Base(DeclarativeBase):
    pass

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///books.db"
# Create the extension
db = SQLAlchemy(model_class=Base)
# initialise the app with the extension
db.init_app(app)

class Book(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    author: Mapped[str] = mapped_column(String(250), nullable=False)
    rating: Mapped[float] = mapped_column(Float, nullable=False)

with app.app_context():
    db.create_all()



class add(FlaskForm):
    Name=StringField("NAME OF THE BOOK", validators=[DataRequired()])
    BOOK=StringField("AUTHOR OF THE BOOK", validators=[DataRequired()])
    RATE=StringField("RATING", validators=[DataRequired()])
    submit=SubmitField("SUBMIT")
    newrate=StringField(" NEW RATING", validators=[DataRequired()])

app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7CsKR6b'
# all_books = []


@app.route('/')
def home():
    result=db.session.execute(db.select(Book).order_by(Book.title))
    all_books=result.scalars().all()
    return render_template("index.html",books=all_books)
    pass



@app.route("/add",methods=["GET", "POST"])
def addme():
    form=add()
    
    if form.validate_on_submit():
        new_book = Book(
    title=form.Name.data,
    author=form.BOOK.data,
    rating=float(form.RATE.data)  # convert string to float
)
        db.session.add(new_book)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template("add.html",form=form)
    pass

@app.route("/edit",methods=["GET","POST"])
def edit():
    form=add()
    if request.method=="POST":
        book_id = request.form.get("id")
        book_to_update = db.get_or_404(Book, book_id)
        book_to_update.rating = request.form["rating"]
        db.session.commit()
        return redirect(url_for('home'))
    book_id = request.args.get('id')
    book_selected = db.get_or_404(Book, book_id)
    return render_template("edit.html", book=book_selected)

@app.route("/delete",methods=["GET","POST"])
def delete():
    book_id=request.args.get('id')
    book_to_delete=db.get_or_404(Book,book_id)
    db.session.delete(book_to_delete)
    
    db.session.commit()
    return redirect (url_for('home'))
if __name__ == "__main__":
    app.run(debug=True)

