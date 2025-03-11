from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, DateField, SubmitField, FileField, PasswordField
from wtforms.validators import DataRequired, Email
from flask_wtf.file import FileField, FileAllowed, FileRequired, FileSize


class CommissionForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired(), Email()])
    request = TextAreaField("Request Details", validators=[DataRequired()])
    questions = StringField("Questions")
    deadline = DateField("Deadline", validators=[DataRequired()])
    submit = SubmitField("Submit")

class PortfolioForm(FlaskForm):

    title = StringField("title")
    style = StringField("style")
    product_type = StringField("product_type")
    artwork = FileField("artwork", validators=[
        FileRequired(),
        FileAllowed(['jpg', 'jpeg', 'png', 'gif'], 'Images only!'),
        FileSize(max_size= .5 * 1024 * 1024)  # .5 MB limit
    ])

