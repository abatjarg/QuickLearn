from django.db import models
from django.template.defaultfilters import slugify

class Category(models.Model):
	name = models.CharField(max_length=100, unique=True)
	slug = models.SlugField(unique=True)

	def __unicode__(self):
		return "%s" % self.name

	class Meta:
		verbose_name_plural = "Categories"

class Card(models.Model):
	front = models.TextField(max_length=200)
	back = models.TextField(max_length=200)
	categories = models.ManyToManyField('Category')

	def __unicode__(self):
		return "%s" % self.front[:10]


