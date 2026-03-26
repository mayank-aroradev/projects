from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, URL
from flask_ckeditor import CKEditorField


class registerform(FlaskForm):
    email=StringField("email",validators=[DataRequired()])
    password=PasswordField("password",validators=[DataRequired()])
    name=StringField("Name",validators=[DataRequired()])
    submit=SubmitField("Submit",validators=[DataRequired()])

class loginform(FlaskForm):
    email=StringField("email",validators=[DataRequired()])
    password=PasswordField("password",validators=[DataRequired()])
    submit=SubmitField("Submit",validators=[DataRequired()])

class commentform(FlaskForm):
    comment=CKEditorField("comment",validators=[DataRequired()])
    submit= SubmitField("submit Comment ")