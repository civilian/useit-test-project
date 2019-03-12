from django.urls import reverse_lazy
from django.views.generic.edit import DeleteView, UpdateView
from django.views.generic.base import TemplateView
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import redirect

from ideas.models import Idea

class DeleteIdea(DeleteView, SuccessMessageMixin):
    success_message = 'The idea has been deleted'
    model = Idea

    def get_success_url(self):
        board_pk = self.get_object().board.id
        return reverse_lazy('boards:crud_user_ideas', kwargs={'board_pk': board_pk})

class UpdateIdea(UpdateView, SuccessMessageMixin):
    success_message = 'The idea has been updated'
    model = Idea
    fields = ['text']
    template_name_suffix = '_update_form'

    def get_success_url(self):
        board_pk = self.get_object().board.id
        return reverse_lazy('boards:crud_user_ideas', kwargs={'board_pk': board_pk})

class ConfirmAcceptIdea(TemplateView):

    template_name = 'ideas/idea_confirm_accept.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['idea'] = Idea.objects.get(id=self.kwargs['pk'])
        return context

def accept_idea(request, pk):
    idea = Idea.objects.get(id=pk)
    idea.accepted = True
    idea.save()
    return redirect(reverse_lazy('boards:crud_user_ideas', kwargs={'board_pk': idea.board.pk}))