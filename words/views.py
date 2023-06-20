from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from django.urls import reverse_lazy
from .models import Word


class WordListView(ListView):
    template_name = "word/word-list.html"
    model = Word


class WordDetailView(DetailView):
    template_name = "word/word-detail.html"
    model = Word


class WordCreateView(CreateView):
    template_name = "word/word-create.html"
    model = Word
    fields = ['word','User','comment']


class WordUpdateView(UpdateView):
    template_name = "word/word-update.html"
    model = Word
    fields = ['word','User','comment']


class WordDeleteView(DeleteView):
    template_name = "word/word-delete.html"
    model = Word
    success_url = reverse_lazy("word_list")
