from flask_wtf import FlaskForm
from wtforms.fields import StringField, IntegerField, HiddenField
from wtforms.validators import DataRequired, ValidationError, NumberRange

class IngredientForm(FlaskForm):
    csrf_token = HiddenField(validators=[DataRequired()])
    measurement_num = IntegerField('measurement_num', validators=[DataRequired()])
    measurement_type = StringField('measurement_type', validators=[DataRequired()])
    ingredient = StringField('ingredient', validators=[DataRequired()])
