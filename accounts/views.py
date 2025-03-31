from django.views.generic import CreateView
from .forms import CustomUserCreationForm
from django.contrib.auth.views import PasswordChangeView, PasswordChangeDoneView
from django.urls import reverse_lazy

# Create your views here.
class SignUpView(CreateView):
    template_name = "registration/signup.html"
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("login")

class CustomPasswordChangeView(PasswordChangeView):
    template_name = "password_change_form.html"
    def get_success_url(self):
        return reverse_lazy("passchangedone")

class CustomPasswordChangeDoneView(PasswordChangeDoneView):
    template_name = "password_change_done.html"
    