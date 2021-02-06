from django.contrib import admin
from .models import Post,Product, Mood ,NewTable


# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ('nickname', 'message', 'enabled', 'pub_time')
    ordering = ('-pub_time',)


admin.site.register(Post, PostAdmin)
admin.site.register(Mood)
admin.site.register(NewTable)
admin.site.register(Product)
