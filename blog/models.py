from django.db import models
from django.contrib.auth.models import User
#from django.utils.translation import gettext_lazy as _


class Note(models.Model):
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    message = models.TextField(default='', verbose_name='Текст')
    public = models.BooleanField(default=False, verbose_name='Опубликовать')
    create_at = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    update_at = models.DateTimeField(auto_now=True, verbose_name='Время обновления')
    #author = models.ForeignKey(User, related_name='authors', on_delete=models.PROTECT, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Сообщение"
        verbose_name_plural = "Сообщения"
