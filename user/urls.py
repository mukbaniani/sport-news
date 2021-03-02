from django.contrib.auth.models import User
from django.urls import path
from .views import RegisterView, UserDetailView, UserUpdateView
from django.contrib.auth import views as auth_view

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', auth_view.LoginView.as_view(template_name="user/login.html"), name='login'),
    path('logout/', auth_view.LogoutView.as_view(template_name="post/home.html"), name='logout'),
    path('account/<int:pk>', UserDetailView.as_view(), name='account'),
    path('user/update/profile/<int:pk>', UserUpdateView.as_view(), name='update-profile'),
    path('password-reset/', auth_view.PasswordResetView.as_view(template_name='user/reset-password.html'), name='password_reset'),
    path('password-reset/done', auth_view.PasswordResetDoneView.as_view(template_name='user/reset-password-done.html'), name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/', 
    auth_view.PasswordResetConfirmView.as_view(template_name='user/update-password.html'),
    name='password_reset_confirm'),
    path('password-reset-complete', auth_view.PasswordResetCompleteView.as_view(template_name='user/password_reset_complete.html'),
    name='password_reset_complete')
]