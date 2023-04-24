from flask_wtf import FlaskForm
from wtforms.fields import StringField
from wtforms.validators import DataRequired, ValidationError

def tag_validator(form, field):
    if len(field.data) < 2 or len(field.data) > 20 :
        raise ValidationError('Tag must be between 2 and 20 characters long')

class CreateTagForm(FlaskForm):
    tag_name = StringField('tag_name', validators=[DataRequired(), tag_validator])

class EditTagForm(FlaskForm):
    tag_name = StringField('tag_name', validators=[DataRequired(), tag_validator])
