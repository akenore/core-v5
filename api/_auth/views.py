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
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import PasswordChangeView
from django.contrib import messages
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.utils.translation import gettext as _
from django.contrib.auth import update_session_auth_hash

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


class SettingsView(LoginRequiredMixin, TemplateView):
    template_name = '_auth/settings.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        return context

    def post(self, request, *args, **kwargs):
        if 'update_profile' in request.POST:
            return self.update_profile(request)
        elif 'change_password' in request.POST:
            return self.change_password(request)
        return self.get(request, *args, **kwargs)

    def update_profile(self, request):
        user = request.user
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        
        if first_name:
            user.first_name = first_name
        if last_name:
            user.last_name = last_name
        if email:
            user.email = email
        
        user.save()
        messages.success(request, _('Profile updated successfully'))
        return redirect('_auth:settings')

    def change_password(self, request):
        form = PasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            messages.success(request, _('Password changed successfully'))
            return redirect('_auth:settings')
        else:
            messages.error(request, _('Please correct the errors below.'))
            return self.get(request, password_form=form)

class CustomPasswordChangeView(PasswordChangeView):
    template_name = '_auth/settings.html'
    success_url = reverse_lazy('_auth:settings')
    
    def form_valid(self, form):
        messages.success(self.request, _('Password changed successfully'))
        return super().form_valid(form)
