from django.contrib import admin
from . models import Job,Category, Apply
# Register your models here.



class ArticleAdmin(admin.ModelAdmin):
    exclude = ('slug',)

admin.site.register(Job)
admin.site.register(Category)
admin.site.register(Apply)

