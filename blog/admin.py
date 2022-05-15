from django.contrib import admin
from .models import Note

#admin.site.register(Note) #Можн так зарегистрировать модель

#Для более тонкой настройки админки можно пойти таким путем
@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    list_display = ['title', 'public', 'create_at', 'update_at']

