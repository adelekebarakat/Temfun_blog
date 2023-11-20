from django.urls import path
from .views import  UserEditProfile, ShowProfilePageView, EditUserProfile,  CreateProfile, Register 
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('register', Register.as_view(), name='register'),
    path('edit_profile', UserEditProfile.as_view(), name='edit_profile'),
    path('password/', auth_views.PasswordChangeView.as_view()),
    path('<str:pk>/profile/', ShowProfilePageView.as_view(), name='profile_page'),
    path('<str:pk>/edituserprofile/', EditUserProfile.as_view(), name='edituserprofile'),
    path('create_profile/', CreateProfile.as_view(), name='create_profile'),
    path('password-reset/',auth_views.PasswordResetView.as_view
         (template_name='registration/password_reset_form.html', html_email_template_name='registration/password_reset_email.html'
),name='password-reset'),
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='registration/password_reset_done.html'),name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='registration/password_reset_confirm.html'),name='password_reset_confirm'),
    path('password-reset-complete/',auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_complete.html'),name='password_reset_complete'),



]
