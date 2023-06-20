from django.contrib import admin
# Register your models here.
from .models import Word

class CustomSnackAdmin(admin.ModelAdmin):
    model = Word
    list_display = ['word', 'User', 'comment',]
    fieldsets= (
        ('Owner',{
            'fields':('User',
            )}
        ),
        ('Word info',{
            'fields':('word','comment',
            )}
        )
    )

    
admin.site.register(Word, CustomSnackAdmin)