from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo, ValidationError

from hoa.models import User

class LoginForm(FlaskForm):
	username = StringField('Username')
	password = PasswordField('Pasword')
	submit = SubmitField('Submit')

class RegistrationForm(FlaskForm):
	username = StringField('Username', validators=[DataRequired()])
	email_address = StringField('Email', validators=[DataRequired(), Email()])
	password = PasswordField('Password', validators=[DataRequired()])
	password2 = PasswordField(
		'Repeat Password', validators=[DataRequired(), EqualTo('password')],
	)
	submit = SubmitField('Register')

	def validate_username(self, username):
		user = User.query.filter_by(username=username.data).first()
		if user is not None:
			raise ValidationError('Please use a different username.')

	def validate_email_address(self, email_address):
		user = User.query.filter_by(email_address=email_address.data).first()
		if user is not None:
			raise ValidationError('Please use a different email address.')

