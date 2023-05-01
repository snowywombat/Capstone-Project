from flask_wtf import FlaskForm
from wtforms.fields import StringField
from wtforms.validators import DataRequired, ValidationError

def title_validator(form, field):
    if len(field.data) < 2 or len(field.data) > 70 :
        raise ValidationError('Title of article must be between 2 and 70 characters long')

def description_validator(form, field):
    if len(field.data) < 3 or len(field.data) > 100 :
        raise ValidationError('Description must be between 3 and 100 characters long.')


class CreateCultureForm(FlaskForm):
    title = StringField('title', validators=[DataRequired(), title_validator])
    description = StringField('description', validators=[DataRequired(), description_validator])
    banner_img = StringField('banner_img', validators=[DataRequired()])
    article = StringField('article', validators=[DataRequired()])

class EditCultureForm(FlaskForm):
    title = StringField('title', validators=[DataRequired(), title_validator])
    description = StringField('description', validators=[DataRequired(), description_validator])
    banner_img = StringField('banner_img', validators=[DataRequired()])
    article = StringField('article', validators=[DataRequired()])
