from django.contrib import admin

from resumes.models import Resume, RidingStyle

admin.site.register(RidingStyle)


@admin.register(Resume)
class ResumeAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'price', 'riding_style')
    fields = ('first_name', 'last_name', 'description', 'price', 'image', 'riding_style')
