from django.views.generic.edit import FormView
from django.urls import reverse
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin

from accounts.forms import SignUpUserForm

class SignUp(SuccessMessageMixin, FormView):
    template_name = 'registration/signup.html'
    form_class = SignUpUserForm
    success_url = '/'
    success_message = 'The user has been created'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
