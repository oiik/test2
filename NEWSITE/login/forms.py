from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import *
from django.forms.widgets import PasswordInput, TextInput


# error_messages = {
# 	'username': {
# 		'required': ('Username is required'),
# 	},
# 	'password': {
# 		'required': ('Password is required'),
# 	},
# 	'password_confirm': {
# 		'required': ('Confirmation is required'),
# 	},
# 	'email': {
# 		'required': ('Email address is required'),
# 		'invalid': ('Email address is invalid'),
# 	},
# 	'interval': {
# 		'invalid': ('delay interval value is invalid'),
# 		'max_value': ('interval value is too large (limit is %(limit_value)s)'),
# 		'min_value': ('interval value is too small (limit is %(limit_value)s)'),
# 	},
# 	'first_last_name': {
# 		'invalid': ('This is too long (limit is %(limit_value)s)'),
# 	},
# 	'code': {
# 		'requered': ('Code is requered'),
# 	},
# }


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2']


class DeadForm(ModelForm):
    class Meta:
        model = Dead
        fields = '__all__'
