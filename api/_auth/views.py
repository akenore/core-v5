from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import views as auth_views
from django.contrib.auth.forms import (
    AuthenticationForm,
    PasswordChangeForm,
    PasswordResetForm,
    SetPasswordForm,
)
from django.urls import reverse_lazy

class LoginView(auth_views.LoginView):
    template_name = '_auth/login.html'
    form_class = AuthenticationForm
    redirect_authenticated_user = True


class LogoutView(auth_views.LogoutView):
    template_name = '_auth/logout.html'


class PasswordChangeView(LoginRequiredMixin, auth_views.PasswordChangeView):
    template_name = '_auth/password_change.html'
    form_class = PasswordChangeForm
    success_url = reverse_lazy('api:password_change_done')


class PasswordChangeDoneView(LoginRequiredMixin, auth_views.PasswordChangeDoneView):
    template_name = '_auth/password_change_done.html'


class PasswordResetView(auth_views.PasswordResetView):
    template_name = '_auth/password_reset.html'
    form_class = PasswordResetForm
    email_template_name = '_auth/password_reset_email.html'
    subject_template_name = '_auth/password_reset_subject.txt'
    success_url = reverse_lazy('_auth:password_reset_done')


class PasswordResetDoneView(auth_views.PasswordResetDoneView):
    template_name = '_auth/password_reset_done.html'


class PasswordResetConfirmView(auth_views.PasswordResetConfirmView):
    template_name = '_auth/password_reset_confirm.html'
    form_class = SetPasswordForm
    success_url = reverse_lazy('api:password_reset_complete')


class PasswordResetCompleteView(auth_views.PasswordResetCompleteView):
    template_name = '_auth/password_reset_complete.html'


