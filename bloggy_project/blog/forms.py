# forms.py - Adds fields to the form

from django import forms
from blog.models import Post

# model form mapped to blog model via the Meta(inner class)
class PostForm(forms.ModelForm):

	class Meta:
		model = Post
		fields = ['title', 'content', 'tag', 'image']