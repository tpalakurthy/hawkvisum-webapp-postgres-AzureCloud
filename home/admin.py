from django.contrib import admin
from .models import team_dynamic, career_content_dynamic, blog_content_dynamic

# About Page #
admin.site.register(team_dynamic)

# Career Page #
admin.site.register(career_content_dynamic)

# Blog Page #
admin.site.register(blog_content_dynamic)

