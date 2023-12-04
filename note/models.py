from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Note(models.Model):
    title = models.CharField(max_length=255, verbose_name='название')
    description = models.TextField(verbose_name='описание', **NULLABLE)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='дата обновления')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'заметка'
        verbose_name_plural = 'заметки'
