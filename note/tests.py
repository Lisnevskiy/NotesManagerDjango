from django.test import TestCase, RequestFactory
from django.urls import reverse

from note.models import Note
from note.views import NoteCreateView


class NoteCreateViewTests(TestCase):
    def setUp(self):
        self.factory = RequestFactory()

    def test_template_used(self):
        response = self.client.get(reverse('note:note_create'))
        self.assertTemplateUsed(response, 'note/note_form.html')

    def test_correct_view_used(self):
        view = NoteCreateView()
        self.assertEqual(view.template_name, 'note/note_form.html')
        self.assertEqual(view.success_url, reverse('note:note_list'))
        self.assertEqual(view.form_class.__name__, 'NoteCreateForm')  # Замените на вашу форму

    def test_note_create(self):
        request = self.factory.post(reverse('note:note_create'), data={'title': 'Test', 'description': 'Test Content'})
        response = NoteCreateView.as_view()(request)
        self.assertEqual(response.status_code, 302)  # Проверяем редирект после успешного создания заметки
        self.assertTrue(Note.objects.filter(title='Test', description='Test Content').exists())


class NoteUpdateViewTests(TestCase):
    def setUp(self):
        self.note = Note.objects.create(title='Test Title', description='Test Content')
        self.update_url = reverse('note:note_update', args=[self.note.pk])
        self.valid_data = {'title': 'Updated Title', 'description': 'Updated Content'}
        self.invalid_data = {'title': '', 'description': ''}

    def test_template_used(self):
        response = self.client.get(self.update_url)
        self.assertTemplateUsed(response, 'note/note_form.html')

    def test_get_request(self):
        response = self.client.get(self.update_url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Title')  # Проверяем, что исходные данные отображаются на странице

    def test_valid_form_submission(self):
        response = self.client.post(self.update_url, self.valid_data)
        self.assertEqual(response.status_code, 302)  # Проверяем редирект после успешного обновления заметки
        self.note.refresh_from_db()  # Обновляем объект из базы данных
        self.assertEqual(self.note.title, 'Updated Title')  # Проверяем, что данные заметки обновились

    def test_invalid_form_submission(self):
        response = self.client.post(self.update_url, self.invalid_data)
        self.assertEqual(response.status_code, 200)  # Проверяем, что страница остаётся доступной при неверных данных
        self.assertFormError(response, 'form', 'title', 'This field is required.')  # Проверяем наличие ошибок формы


class NoteListViewTests(TestCase):
    def setUp(self):
        self.note1 = Note.objects.create(title='Test Title', description='Content 1')
        self.note2 = Note.objects.create(title='Test Title 2', description='Content 2')

    def test_notes_displayed(self):
        response = self.client.get(reverse('note:note_list'))
        self.assertEqual(response.status_code, 200)


class NoteDetailViewTests(TestCase):
    def setUp(self):
        self.note = Note.objects.create(title='Test Title', description='Test Content')
        self.detail_url = reverse('note:note_detail', args=[self.note.pk])

    def test_template_used(self):
        response = self.client.get(self.detail_url)
        self.assertTemplateUsed(response, 'note/note_detail.html')

    def test_note_displayed(self):
        response = self.client.get(self.detail_url)
        self.assertContains(response, 'Test Title')
        self.assertContains(response, 'Test Content')


class NoteDeleteViewTests(TestCase):
    def setUp(self):
        self.note = Note.objects.create(title='Test Title', description='Test Content')
        self.delete_url = reverse('note:note_delete', args=[self.note.pk])

    def test_template_used(self):
        response = self.client.get(self.delete_url)
        self.assertTemplateUsed(response, 'note/note_confirm_delete.html')

    def test_note_deleted(self):
        # Подтверждение удаления с передачей данных (в данном случае, параметр 'delete' со значением 'yes')
        response = self.client.post(self.delete_url, {'delete': 'yes'})
        self.assertRedirects(response, reverse('note:note_list'))
        self.assertFalse(Note.objects.filter(pk=self.note.pk).exists())
