from django.urls import path
from .views import home, debug_base
from . import views
from django.contrib.auth.views import (
    LogoutView, 
    PasswordResetView, 
    PasswordResetDoneView, 
    PasswordResetConfirmView,
    PasswordResetCompleteView
)
from .views import user_dashboard
from .views import user_logout

urlpatterns = [
    path('', home, name='home'),
    path('debug-base/', debug_base, name='debug-base'),
    path('register/', views.register, name='register'),
    path('dashboard/', user_dashboard, name='dashboard'),
    path('logout/', user_logout, name='logout'),
    path('login/', views.user_login, name='login'),
    path('complete-profile/', views.complete_profile, name='complete_profile'),
    path('password-reset/', PasswordResetView.as_view(template_name='registration/password_reset.html'),name='password_reset'),
    path('password-reset/done/', PasswordResetDoneView.as_view(template_name='registration/password_reset_done.html'),name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/', PasswordResetConfirmView.as_view(template_name='registration/password_reset_confirm.html'),name='password_reset_confirm'),
    path('password-reset-complete/', PasswordResetCompleteView.as_view(template_name='registration/password_reset_complete.html'),name='password_reset_complete'),
  

    
]
