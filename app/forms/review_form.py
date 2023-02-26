from flask_wtf import FlaskForm
from wtforms.fields import StringField, IntegerField
from wtforms.validators import DataRequired, ValidationError

def review_validator(form, field):
    if len(field.data) < 3 or len(field.data) > 100 :
        raise ValidationError('Review must be between 3 and 100 characters long')

def location_validator(form, field):
    if len(field.data) < 3 or len(field.data) > 50 :
        raise ValidationError('Location must be between 3 and 50 characters long.')

def stars_validator(form, field):
    if field.data < 1 or field.data > 5 :
        raise ValidationError('Stars must be between 1 and 5.')

class CreateReviewForm(FlaskForm):
    review = StringField('review', validators=[DataRequired(), review_validator])
    stars = IntegerField('stars', validators=[DataRequired(), stars_validator])
    location = StringField('location', validators=[DataRequired(), location_validator])

class EditReviewForm(FlaskForm):
    review = StringField('review', validators=[DataRequired(), review_validator])
    stars = IntegerField('stars', validators=[DataRequired(), stars_validator])
    location = StringField('location', validators=[DataRequired(), location_validator])
