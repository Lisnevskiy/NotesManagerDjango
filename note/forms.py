from django.forms import ModelForm

from note.models import Note


class NoteCreateForm(ModelForm):

    class Meta:
        model = Note
        fields = ['title', 'description']
