# To access the admin-web based

from django.contrib import admin
from blog.models import Post

# Register your models here - Show which models we want available in the admin

# Customise Admin View
class PostAdmin(admin.ModelAdmin):
	list_display = ('title', 'created_at', 'views') # fields we want displayed


# Register PostAdmin class with django admin interface
admin.site.register(Post, PostAdmin)