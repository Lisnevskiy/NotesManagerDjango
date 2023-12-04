from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from note.forms import NoteCreateForm
from note.models import Note
from note.services import get_it_news


async def get_news(request):
    it_news = await get_it_news()

    return render(request, 'note/news.html', {'it_news': it_news})


class NoteListView(ListView):
    model = Note
    extra_context = {'title': 'Рассылки'}


class NoteDetailView(DetailView):
    model = Note
    template_name = 'note/note_detail.html'  # Шаблон для отображения отдельной заметки


class NoteCreateView(CreateView):
    model = Note
    form_class = NoteCreateForm
    success_url = reverse_lazy('note:note_list')  # URL для перенаправления после удаления заметки
    template_name = 'note/note_form.html'  # Шаблон для создания заметки


class NoteUpdateView(UpdateView):
    model = Note
    form_class = NoteCreateForm
    template_name = 'note/note_form.html'  # Шаблон для обновления заметки

    def get_success_url(self):
        return reverse('note:note_detail', args=[self.kwargs.get('pk')])


class NoteDeleteView(DeleteView):
    model = Note
    template_name = 'note/note_confirm_delete.html'  # Шаблон для подтверждения удаления заметки
    success_url = reverse_lazy('note:note_list')  # URL для перенаправления после удаления заметки
