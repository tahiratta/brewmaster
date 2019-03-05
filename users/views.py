from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from django.contrib.auth import logout
from custdata.models import *


# Create your views here.
def register(request):
	if request.method == 'POST':
		form = UserRegisterForm(request.POST)
		if form.is_valid():
			form.save()
			print('form',form)
			username = form.cleaned_data.get('username')
			messages.success(request, f'Your account has been created! You are now able to log in')
			return redirect('login')
	else:
		print('not registered')
		form = UserRegisterForm()
	return render(request, 'users/register.html', {'form': form})

@login_required
def profile(request):
	if request.method == 'POST':
		u_form = UserUpdateForm(request.POST, instance=request.user)
		# p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
		# print('Pform', p_form)
		print('uform', u_form)

		# and p_form.is_valid()
		if u_form.is_valid():
			u_form.save()
			# p_form.save()
			messages.success(request, f'Your account has been updated!')
			return redirect('profile')
	else:
		u_form = UserUpdateForm(instance=request.user)
		print("u_form", u_form)
		# p_form = ProfileUpdateForm(instance=request.user.profile)

	context = {
		'u_form': u_form,
		# 'p_form': p_form
	}
	return render(request, 'users/profile.html', context)

def my_logout(request):
	Orders.objects.all().delete()
	Customers.objects.all().delete()
	response = logout(request)
	return render(response, 'users/logout.html')