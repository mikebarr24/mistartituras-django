from django.contrib import admin

from .models import Part, Instrument, Level, Style, Curso

admin.site.register(Part)
admin.site.register(Instrument)
admin.site.register(Level)
admin.site.register(Style)
admin.site.register(Curso)
