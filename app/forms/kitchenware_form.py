from flask_wtf import FlaskForm
from wtforms.fields import StringField, IntegerField
from wtforms.validators import DataRequired, ValidationError, NumberRange

class KitchenwareForm(FlaskForm):
    name = StringField('name', validators=[DataRequired()])
