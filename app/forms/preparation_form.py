from flask_wtf import FlaskForm
from wtforms.fields import StringField, IntegerField
from wtforms.validators import DataRequired, ValidationError, NumberRange

class PreparationForm(FlaskForm):
    description = StringField('description', validators=[DataRequired()])
