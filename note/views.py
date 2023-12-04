from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from note.forms import NoteCreateForm
from note.models import Note
from note.services import get_it_news


async def get_news(request):
    """
    Асинхронное представление, которое получает информацию о новостях из области IT
    с помощью вспомогательной функции get_it_news и рендерит шаблон 'note/news.html'.
    Args:
        request: HttpRequest объект.
    Returns:
        HttpResponse: Ответ с отображением новостей IT.
    """
    it_news = await get_it_news()
    return render(request, 'note/news.html', {'it_news': it_news})


class NoteListView(ListView):
    """
    Представление для отображения списка заметок.
    Attributes:
        model (Model): Модель, используемая для получения данных.
    """
    model = Note


class NoteDetailView(DetailView):
    """
    Представление для отображения отдельной заметки.
    Attributes:
        model (Model): Модель, используемая для получения данных.
        template_name (str): Имя шаблона для отображения деталей заметки.
    """
    model = Note
    template_name = 'note/note_detail.html'


class NoteCreateView(CreateView):
    """
    Представление для создания новой заметки.
    Attributes:
        model (Model): Модель, используемая для создания заметки.
        form_class (Form): Форма, используемая для создания заметки.
        success_url (str): URL для перенаправления после успешного создания заметки.
        template_name (str): Имя шаблона для создания заметки.
    """
    model = Note
    form_class = NoteCreateForm
    success_url = reverse_lazy('note:note_list')
    template_name = 'note/note_form.html'


class NoteUpdateView(UpdateView):
    """
    Представление для обновления заметки.
    Attributes:
        model (Model): Модель, используемая для обновления заметки.
        form_class (Form): Форма, используемая для обновления заметки.
        template_name (str): Имя шаблона для обновления заметки.
    """
    model = Note
    form_class = NoteCreateForm
    template_name = 'note/note_form.html'

    def get_success_url(self):
        return reverse('note:note_detail', args=[self.kwargs.get('pk')])


class NoteDeleteView(DeleteView):
    """
    Представление для удаления заметки.
    Attributes:
        model (Model): Модель, используемая для удаления заметки.
        template_name (str): Имя шаблона для подтверждения удаления заметки.
        success_url (str): URL для перенаправления после удаления заметки.
    """
    model = Note
    template_name = 'note/note_confirm_delete.html'
    success_url = reverse_lazy('note:note_list')
