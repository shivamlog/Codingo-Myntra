from django.contrib import admin

# Register your models here.
from .models import BlogModel, CommentModel, LikeModel

admin.site.register(BlogModel)
admin.site.register(CommentModel)
admin.site.register(LikeModel)