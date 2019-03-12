from django.urls import reverse_lazy
from django.views.generic.edit import DeleteView
from django.contrib.messages.views import SuccessMessageMixin

from ideas.models import Idea

class DeleteIdea(DeleteView, SuccessMessageMixin):
    success_message = 'The idea has been deleted'
    model = Idea

    def get_success_url(self):
        board_pk = self.get_object().board.id
        return reverse_lazy('boards:crud_user_ideas', kwargs={'board_pk': board_pk})