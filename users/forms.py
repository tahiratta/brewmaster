from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile
from django.contrib.auth.forms import PasswordResetForm
from django.utils.translation import gettext as _

class EmailValidationOnForgotPassword(PasswordResetForm):

    def clean_email(self):
        email = self.cleaned_data['email']
        if not User.objects.filter(email__iexact=email, is_active=True).exists():
            msg = _("There is no user registered with the specified email address.")
            self.add_error('email', msg)
        return email

class UserRegisterForm(UserCreationForm):
	email = forms.EmailField()

	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']

	def clean_email(self):
		data = self.cleaned_data['email']
		duplicate_users = User.objects.filter(email__iexact=data)
		# if self.instance.pk is not None:  # If you're editing an user, remove him from the duplicated results
		# 	duplicate_users = duplicate_users.exclude(pk=self.instance.pk)
		if duplicate_users.exists():
			raise forms.ValidationError("A user with that email is already registered!")
		return data
		

class UserUpdateForm(forms.ModelForm):
	email = forms.EmailField()

	class Meta:
		model = User
		fields = ['username', 'email']


class ProfileUpdateForm(forms.ModelForm):
	class Meta:
		model = Profile
		fields = ['image']
