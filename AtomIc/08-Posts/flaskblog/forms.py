from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from flask_login import current_user
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField
from wtforms import IntegerField, DateField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from flaskblog.models import User
from wtforms import SelectField
from flask_wtf import Form

class RegistrationForm(FlaskForm):
	username = StringField('Username',
						   validators=[DataRequired(), Length(min=2, max=20)])
	email = StringField('Email',
						validators=[DataRequired(), Email()])
	password = PasswordField('Password', validators=[DataRequired()])
	confirm_password = PasswordField('Confirm Password',
									 validators=[DataRequired(), EqualTo('password')])
									 
	ch = [('ron','RON'), ('eur','EURO'),('dollar','DOLLAR')]
	place = SelectField('Select currency', choices = ch)
	
	submit = SubmitField('Sign Up')

	def validate_username(self, username):
		user = User.query.filter_by(username=username.data).first()
		if user:
			raise ValidationError('That username is taken. Please choose a different one.')

	def validate_email(self, email):
		user = User.query.filter_by(email=email.data).first()
		if user:
			raise ValidationError('That email is taken. Please choose a different one.')


class LoginForm(FlaskForm):
	email = StringField('Email',
						validators=[DataRequired(), Email()])
	password = PasswordField('Password', validators=[DataRequired()])
	remember = BooleanField('Remember Me')
	submit = SubmitField('Login')
	
class ClientInvestorButton(FlaskForm):
	username=StringField('vec')
	password=StringField('vec')
	confirm_password=StringField('vec')
	type=StringField('vec')
	place=StringField('vec')
	email=StringField('vec')
	client = SubmitField(label='Client')
	investor = SubmitField(label='Investor')

class UpdateAccountForm(FlaskForm):
	username = StringField('Username',
						   validators=[DataRequired(), Length(min=2, max=20)])
	balance = IntegerField('Add money')
	picture = FileField('Update Profile Picture', validators=[FileAllowed(['jpg', 'png'])])
	ch = [('0','ID Card'), ('1','Income receipt'),('2','Contract')]
	documentType = SelectField('Select document:', choices = ch)
	document = FileField('Insert document', validators=[FileAllowed(['jpg', 'png'])])
	submit = SubmitField('Update')

	def validate_username(self, username):
		if username.data != current_user.username:
			user = User.query.filter_by(username=username.data).first()
			if user:
				raise ValidationError('That username is taken. Please choose a different one.')

	def validate_email(self, email):
		if email.data != current_user.email:
			user = User.query.filter_by(email=email.data).first()
			if user:
				raise ValidationError('That email is taken. Please choose a different one.')


class PostForm(FlaskForm):
	sum = IntegerField('Sum', validators=[DataRequired()])
	interest = IntegerField('Interest', validators=[DataRequired()])
	payDate = DateField('Pay date (YYYY-MM-DD)', format='%Y-%m-%d')
	description = TextAreaField('Description', validators=[DataRequired()])
	submit = SubmitField('Post')
