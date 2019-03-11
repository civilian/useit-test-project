from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin

from boards.models import Board
from ideas.models import Idea

class ShowBoardsPageView(TemplateView):

    template_name = 'boards/show_boards.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        context['user_boards'] = Board.objects.filter(owner=user) 
        context['public_boards'] = (Board.objects.exclude(owner=user)
                                        .filter(private=False))
        return context

class CreateBoardPageView(SuccessMessageMixin, CreateView):
    success_message = 'The board has been created'
    template_name = 'boards/create_board.html'
    model = Board
    fields = ['title', 'private']
    success_url = '/boards/'

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super(CreateBoardPageView, self).form_valid(form)

class CrudIdeasPageView(TemplateView):
    template_name = 'boards/crud_ideas.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # TODO: create acepted and the other ideas
        board = Board.objects.get(id=self.kwargs['board_id'])
        context['ideas'] = Idea.objects.filter(board=board)
        context['board'] = board
        return context