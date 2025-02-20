from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, DateField, SubmitField
from wtforms.validators import DataRequired, Email

class CommissionForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired(), Email()])
    request = TextAreaField("Request Details", validators=[DataRequired()])
    questions = StringField("Questions")
    deadline = DateField("Deadline", validators=[DataRequired()])
    submit = SubmitField("Submit")
