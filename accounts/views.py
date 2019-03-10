from django.views.generic.edit import FormView
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin

from accounts.forms import SignUpUserForm

class SignUpPageView(SuccessMessageMixin, FormView):
    template_name = 'registration/signup.html'
    form_class = SignUpUserForm
    success_url = '/'
    success_message = 'The user has been created'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
