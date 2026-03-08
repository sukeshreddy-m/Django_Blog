from django.contrib import admin
from .models import about,social

class AboutAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        count = about.objects.all().count()
        if count==0:
            return True
        return False

admin.site.register(about, AboutAdmin)
admin.site.register(social)