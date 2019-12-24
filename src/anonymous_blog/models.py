from django.db import models


class Message(models.Model):
    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'
        ordering = (
            '-create_date',
        )

    text = models.TextField(verbose_name='Сообщение')
    create_date = models.DateTimeField(verbose_name='Дата добавления сообщения', auto_now_add=True)

    def __str__(self):
        return self.text
