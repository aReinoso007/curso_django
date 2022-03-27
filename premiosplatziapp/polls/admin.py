from django.contrib import admin

from .models import Choice, Question

#Esto para poder revisar los modelos desde la pagina de administracion de django
admin.site.register(Question)
admin.site.register(Choice)