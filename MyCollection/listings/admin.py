from django.contrib import admin
from .models import Genre


class GenreAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)


admin.site.register(Genre, GenreAdmin)
