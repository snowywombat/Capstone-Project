from flask_wtf import FlaskForm
from wtforms.fields import StringField, IntegerField, FieldList, FormField
from wtforms.validators import DataRequired, ValidationError
from .ingredient_form import IngredientForm
from .kitchenware_form import KitchenwareForm
from .preparation_form import PreparationForm

def name_validator(form, field):
    if len(field.data) < 3 or len(field.data) > 50 :
        raise ValidationError('Name of recipe must be between 3 and 50 characters long')

def description_validator(form, field):
    if len(field.data) < 3 or len(field.data) > 200 :
        raise ValidationError('Description must be between 3 and 200 characters long.')

def servings_num_validator(form, field):
    if field.data < 1 or field.data > 100 :
        raise ValidationError('Serving size must be between 1 and 100.')

def ingredient_validator(form, field):
      if not any(field.data):
          raise ValidationError('Please add at least one ingredient')

class CreateRecipeForm(FlaskForm):
  name = StringField('name', validators=[DataRequired(), name_validator])
  description = StringField('description', validators=[DataRequired(), description_validator])
  servings_num = IntegerField('servings_num', validators=[DataRequired(), servings_num_validator])
  img_url = StringField('img_url', validators=[DataRequired()])
  kitchenware_form = FieldList(FormField(KitchenwareForm))
  ingredient_form = FieldList(FormField(IngredientForm), min_entries=1, validators=[DataRequired(), ingredient_validator])
  preparation_form = FieldList(FormField(PreparationForm))

class EditRecipeForm(FlaskForm):
  name = StringField('name', validators=[DataRequired(), name_validator])
  description = StringField('description', validators=[DataRequired(), description_validator])
  servings_num = IntegerField('servings_num', validators=[DataRequired(), servings_num_validator])
  img_url = StringField('img_url', validators=[DataRequired()])
