from django.contrib import admin
from .models import Example


@admin.register(Example)
class AdminForExample(admin.ModelAdmin):
    list_display = ("title", "author", "created_at")
    # prepopulated_fields = {
    #     "slug": ("title",),
    # }


# admin.site.register(AnotherModel)
