from django.urls import path
from .views import SignUpView, PasswordChangeView
from django.contrib.auth.views import PasswordResetView, PasswordResetConfirmView


urlpatterns = [
    path("signup/", SignUpView.as_view(), name="signup"),
    path("registration/password_change_form/", PasswordChangeView.as_view(), name="passchange"),
    path("password_reset/", PasswordResetView.as_view(), name="passreset"),
    path("reset/<uidb64>/<token>/", PasswordResetConfirmView.as_view(template_name="password_reset_confirm.html"), name="passresetconfirm"),
]