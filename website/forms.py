from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, DateField, SubmitField, FileField, SelectField
from wtforms.validators import DataRequired, Email
from flask_wtf.file import FileField, FileAllowed, FileRequired, FileSize


class CommissionForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired(), Email()])
    request = TextAreaField("Request Details", validators=[DataRequired()])
    questions = StringField("Questions")
    deadline = DateField("Deadline", validators=[DataRequired()])


class PortfolioForm(FlaskForm):
    title = StringField("title")
    product_type = SelectField(
        "Commission Type", 
        choices=[
            ("emote", "Emote"),
            ("vtuber", "Vtuber Model Feature"),
            ("logo", "Logo Design"),
            ("pfp", "Profile Picture"),
            ("sketch", "Sketch"),
            ("other", "Other"),
        ], 
        validators=[DataRequired()]
    )
    artwork = FileField("artwork", validators=[
        FileRequired(),
        FileAllowed(['jpg', 'jpeg', 'png', 'gif'], 'Images only!'),
        FileSize(max_size= 25 * 1024 * 1024)  # 25 MB limit
    ])

