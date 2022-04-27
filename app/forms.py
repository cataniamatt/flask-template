from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField, RadioField
from wtforms.validators import DataRequired

# A class is created for each form required
class TestForm(FlaskForm):
	genders = [
		('male', 'Male'),
		('female', 'Female')
	]

	sports = [
		('football', 'Football'),
		('basketball', 'Basketball')
	]

	name = StringField('Name', validators=[DataRequired()])
	surname = StringField('Surname', validators=[DataRequired()])
	gender = RadioField('Gender', choices=genders, validators=[DataRequired()])
	sport = SelectField('Sport', choices=sports, validators=[DataRequired()])
	submit = SubmitField('Submit')
