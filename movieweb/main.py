from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import requests
import os
api_key = os.getenv("MOV_KEY")
headers = {"accept": "application/json"}
'''
Red underlines? Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)

# CREATE DB

class Base(DeclarativeBase):
    pass
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///movies.db'
db=SQLAlchemy(model_class=Base)
db.init_app(app)

class Movie(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    year: Mapped[int] = mapped_column(Integer, nullable=False)
    description: Mapped[str] = mapped_column(String(500), nullable=False)
    rating: Mapped[float] = mapped_column(Float, nullable=True)
    ranking: Mapped[int] = mapped_column(Integer, nullable=True)
    review: Mapped[str] = mapped_column(String(250), nullable=True)
    img_url: Mapped[str] = mapped_column(String(250), nullable=False)

with app.app_context():
    db.create_all()

# CREATE TABLE
new_movie=Movie(title="Phone Booth",
    year=2002,
    description="Publicist Stuart Shepard finds himself trapped in a phone booth, pinned down by an extortionist's sniper rifle. Unable to leave or receive outside help, Stuart's negotiation with the caller leads to a jaw-dropping climax.",
    rating=7.3,
    ranking=10,
    review="My favourite character was the caller.",
    img_url="https://image.tmdb.org/t/p/w500/tjrX2oWRCM3Tvarz38zlZM7Uc10.jpg"
)
second_movie = Movie(
    title="Avatar The Way of Water",
    year=2022,
    description="Set more than a decade after the events of the first film, learn the story of the Sully family (Jake, Neytiri, and their kids), the trouble that follows them, the lengths they go to keep each .",
    rating=7.3,
    ranking=9,
    review="I liked the water.",
    img_url="https://image.tmdb.org/t/p/w500/t6HIqrRAclMCA60NsSmeqe9RmNV.jpg"
)
# with app.app_context():
# #     db.session.add(new_movie)
#     db.session.add(second_movie)
#     db.session.commit()
class ratemovie(FlaskForm):
    rating=StringField("RATE THIS MOVIE")
    review=StringField("REVIEW THIS MOVIE")
    submit=SubmitField("submit")

class addmov(FlaskForm):
    title=StringField('ENTER NAME OF THE MOVIE')
    submitbut=SubmitField('submit')

@app.route("/")
def home():
    result=db.session.execute(db.select(Movie).order_by(Movie.ranking.desc()))
    all_movies=result.scalars().all()
    for i in range (len(all_movies)):
        all_movies[i].ranking=i+1
        db.session.commit()
    return render_template("index.html",movies=all_movies)

@app.route("/edit",methods=["GET","POST"])
def editme():
    form=ratemovie()
    movie_id=request.args.get("id")
    movie= db.get_or_404(Movie,movie_id)
    if form.validate_on_submit():
        movie.rating=float(form.rating.data)
        movie.review=form.review.data
        db.session.commit()
        return redirect (url_for('home'))
    return render_template("edit.html", movie=movie, form=form)

@app.route("/delete",methods=["GET","POST"])
def deleteme():
    movie_id2=request.args.get('id')
    movie_to_del=db.get_or_404(Movie,movie_id2)
    db.session.delete(movie_to_del)
    db.session.commit()
    return redirect (url_for("home"))

url="https://api.themoviedb.org/3/search/movie"
movie_r="https://api.themoviedb.org/3/movie"
@app.route("/add",methods=["GET","POST"])
def addme():
    form2=addmov()
    if form2.validate_on_submit():
        movie_title=form2.title.data
        response = requests.get(url, params={
            "api_key": "b0673af4f6e6742fe32ee8d13443a395",  # from environment
            "query": movie_title
        },timeout=10)
        print(response.status_code)
        data=response.json()['results']
        print(data)
        return render_template("select.html",options=data)
    
    return render_template('add.html',form=form2)

@app.route("/find",methods=["GET","POST"])
def findme():
    movie_api_id=request.args.get('id')
    if movie_api_id:
        movie_url=f'{movie_r}/{movie_api_id}'
        response=requests.get(movie_url,params={"api_key":'b0673af4f6e6742fe32ee8d13443a395',"language": "en-US"},timeout=10)
        data=response.json()
        print(data)
        print("STATUS:", response.status_code)  # 👈 Add this
        print("DATA:", data)    
        new_movie=Movie(
            title=data["title"],
            year=data["release_date"].split("-")[0],
            img_url=f"https://image.tmdb.org/t/p/original{data['poster_path']}",
            description=data["overview"]
           )
        db.session.add(new_movie)
        db.session.commit()
        return redirect(url_for("home"))


if __name__ == '__main__':
    app.run(debug=True)
