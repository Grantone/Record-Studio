from django.contrib import admin
from .models import Studio, User, tags

# Register your models here.


class StudioAdmin(admin.ModelAdmin):
    filter_horizontal = ('tags',)


admin.site.register(Studio, StudioAdmin)
admin.site.register(User)
admin.site.register(tags)
