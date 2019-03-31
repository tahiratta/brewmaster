from django.contrib.auth import views as auth_views
from django.urls import path
from users.forms import EmailValidationOnForgotPassword

urlpatterns = [
    path('password-reset/', auth_views.PasswordResetView.as_view(template_name='users/password_reset_form.html', form_class=EmailValidationOnForgotPassword),
         name='password_reset'),
    path('password-reset/done',
         auth_views.PasswordResetDoneView.as_view(template_name='users/password_reset_done.html'),
         name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html'),
         name='password_reset_confirm'),
    path('reset/done/',
         auth_views.PasswordResetCompleteView.as_view(template_name='users/password_reset_complete.html'),
         name='password_reset_complete'),
]