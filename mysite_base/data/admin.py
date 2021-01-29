from django.contrib import admin
from .models import IT
from .models import ECO
from .models import SPORTS

# class ITadmin(admin.ModelAdmin):
#         list_display = ('title', 'preview', 'crawled_time')

# Register your models here.
admin.site.register(IT)
admin.site.register(ECO)
admin.site.register(SPORTS)