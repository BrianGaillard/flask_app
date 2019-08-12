from flask_wtf import FlaskForm
from wtforms import IntegerField, SubmitField
from wtforms.validators import DataRequired, Length, NumberRange

class YearForm(FlaskForm):
	year = IntegerField('Year', 
						validators=[DataRequired(), Length(min=4, max=5), NumberRange(min=2019, max=9999)])
	submit = SubmitField('GO')