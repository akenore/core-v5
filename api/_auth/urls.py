from django.urls import path
from . import views

app_name = '_auth'

urlpatterns = [
    
    path('auth/login/', views.LoginView.as_view(), name='login'),
    path('auth/logout/', views.LogoutView.as_view(), name='logout'),
    path('auth/password-change/', views.PasswordChangeView.as_view(), name='password_change'),
    path('auth/password-change/done/', views.PasswordChangeDoneView.as_view(), name='password_change_done'),
    path('auth/password-reset/', views.PasswordResetView.as_view(), name='password_reset'),
    path('auth/password-reset/done/', views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('auth/reset/<uidb64>/<token>/', views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('auth/reset/done/', views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]
