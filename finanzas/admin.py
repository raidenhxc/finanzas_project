from django.contrib import admin

# Register your models here.
from models import Concept, Movement, Exercise, Period

admin.site.register(Concept)
admin.site.register(Movement)
admin.site.register(Exercise)
admin.site.register(Period)