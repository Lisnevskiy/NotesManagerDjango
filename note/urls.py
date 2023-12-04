from django.urls import path
from django.views.decorators.cache import cache_page

from .apps import NoteConfig
from .views import NoteListView, NoteDetailView, NoteCreateView, NoteUpdateView, NoteDeleteView, get_news

app_name = NoteConfig.name

urlpatterns = [
    path('news/', get_news, name='news'),
    path('', cache_page(60)(NoteListView.as_view()), name='note_list'),
    path('<int:pk>/', NoteDetailView.as_view(), name='note_detail'),
    path('create/', NoteCreateView.as_view(), name='note_create'),
    path('<int:pk>/update/', NoteUpdateView.as_view(), name='note_update'),
    path('<int:pk>/delete/', NoteDeleteView.as_view(), name='note_delete'),
]
