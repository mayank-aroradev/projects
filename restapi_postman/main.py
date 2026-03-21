from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Boolean
import os
import random
'''
Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''


basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__, instance_path=os.path.join(basedir, 'instance'))

# CREATE DB
class Base(DeclarativeBase):
    pass
# Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
app.config["SQLALCHEMY_ENGINE_OPTIONS"] = {
    "connect_args": {"timeout": 15}  # seconds to wait before giving up
}
db = SQLAlchemy(model_class=Base)
db.init_app(app)


# Cafe TABLE Configuration
class Cafe(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    map_url: Mapped[str] = mapped_column(String(500), nullable=False)
    img_url: Mapped[str] = mapped_column(String(500), nullable=False)
    location: Mapped[str] = mapped_column(String(250), nullable=False)
    seats: Mapped[str] = mapped_column(String(250), nullable=False)
    has_toilet: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_wifi: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_sockets: Mapped[bool] = mapped_column(Boolean, nullable=False)
    can_take_calls: Mapped[bool] = mapped_column(Boolean, nullable=False)
    coffee_price: Mapped[str] = mapped_column(String(250), nullable=True)

    def get_dict(self):
        return {column.name:getattr(self,column.name) for column in self.__table__.columns}


with app.app_context():
    db.create_all()


@app.route("/")
def home():
    return render_template("index.html")


# HTTP GET - Read Record
@app.route("/random")
def randomme():
    result=db.session.execute(db.select(Cafe))
    cafes=result.scalars().all()
    random_cafe=random.choice(cafes)
    return jsonify(cafe=random_cafe.get_dict())
        
@app.route("/all")
def alldat():
    result2=db.session.execute(db.select(Cafe))
    cafes2=result2.scalars().all()
    return jsonify(cafes=[cafe.get_dict() for cafe in cafes2])
@app.route ("/search/<loc>")
def get_loc(loc):
    query_loc=loc
    result=db.session.execute(db.select(Cafe).where(Cafe.location==query_loc))
    cafes=result.scalars().all()
    
    return jsonify(cafep=[cafe.get_dict() for cafe in cafes])
@app.route("/add", methods=["POST"])
def add_me():
    print(request.form)  # <-- add this
    print(request.form.get("location")) 
    new_cafe= Cafe(
        name=request.form.get("name"),
        map_url=request.form.get("map_url"),
        img_url=request.form.get("img_url"),
        location=request.form.get("loc"),
        has_sockets=bool(request.form.get("sockets")),
        has_toilet=bool(request.form.get("toilet")),
        has_wifi=bool(request.form.get("wifi")),
        can_take_calls=bool(request.form.get("calls")),
        seats=request.form.get("seats"),
        coffee_price=request.form.get("coffee_price"),
    )
    db.session.add(new_cafe)
    db.session.commit()
    return jsonify(response={"success": "Successfully added the new cafe."})
    

@app.route("/update-price/<int:cafe_id>",methods=["PATCH"])
def patch_new(cafe_id):
    new_price=request.args.get("new_price")
    cafe=db.session.get(entity=Cafe,ident=cafe_id)
    if cafe:
        cafe.coffee_price= new_price
        db.session.commit()
        return jsonify(response={"success":"Successfully updated the price "})
    else:
        return jsonify(error={"Not Found": "Sorry a cafe with that id was not found in the database."}), 404

# HTTP POST - Create Record

# HTTP PUT/PATCH - Update Record

# HTTP DELETE - Delete Record


if __name__ == '__main__':
    app.run(debug=True,threaded=False)
