from django.contrib import admin
from .models import Movie


@admin.register(Movie)
class AdminForMovie(admin.ModelAdmin):
    list_display = ("title", "author", "created_at")
    # prepopulated_fields = {
    #     "slug": ("title",),
    # }


# admin.site.register(AnotherModel)
