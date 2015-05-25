from django.db import models

from uuslug import uuslug

# Create your models here.e.g what can be stored in the database using django ORM


# class post-defines the db table as well as each field
class Post(models.Model):
	created_at = models.DateTimeField(auto_now_add=True)
	title = models.CharField(max_length=100)
	content = models.TextField()
	# updating the table
	tag = models.CharField(max_length=20, blank=True, null=True)
	image = models.ImageField(upload_to="images", blank=True, null=True)
	views = models.IntegerField(default=0)
	slug = models.CharField(max_length=100, unique=True)


	# using unicode bcz django models use unicode by default
	def __unicode__(self):
		return self.title


	def save(self, *args, **kwargs):
		self.slug = uuslug(self.title, instance=self, max_length=100)
		super(Post, self).save(*args, **kwargs)