from django.contrib import admin
from .models import Post, Comment, Profile

from django_summernote.admin import SummernoteModelAdmin

class SomeModelAdmin(SummernoteModelAdmin):
	...

# Register your models here.
#admin.site.register(Post)
admin.site.register(Profile)
admin.site.register(Comment)
admin.site.register(Post, SomeModelAdmin)
