from flask_wtf import FlaskForm
from wtforms.fields import StringField, IntegerField
from wtforms.validators import DataRequired, ValidationError

def name_validator(form, field):
    if len(field.data) < 3 or len(field.data) > 50 :
        raise ValidationError('Name of recipe must be between 3 and 50 characters long')

def description_validator(form, field):
    if len(field.data) < 3 or len(field.data) > 200 :
        raise ValidationError('Description must be between 3 and 200 characters long.')

def servings_num_validator(form, field):
    if field.data < 1 or field.data > 100 :
        raise ValidationError('Serving size must be between 1 and 100.')

class CreateRecipeForm(FlaskForm):
  name = StringField('name', validators=[DataRequired(), name_validator])
  description = StringField('description', validators=[DataRequired(), description_validator])
  servings_num = IntegerField('servings_num', validators=[DataRequired(), servings_num_validator])
  img_url = StringField('img_url', validators=[DataRequired()])

class EditRecipeForm(FlaskForm):
  name = StringField('name', validators=[DataRequired(), name_validator])
  description = StringField('description', validators=[DataRequired(), description_validator])
  servings_num = IntegerField('servings_num', validators=[DataRequired(), servings_num_validator])
  img_url = StringField('img_url', validators=[DataRequired()])
