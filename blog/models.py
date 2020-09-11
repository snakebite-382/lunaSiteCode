from django.db import models
from django.urls import reverse
from django.utils import timezone

# Create your models here.
class Article(models.Model):
	title = models.CharField(max_length=75, blank=False)
	author = models.CharField(max_length=100, blank=False, default="Luna Lovegood Limerick")
	main = models.TextField(blank=False)
	teaserSummary = models.CharField(max_length=250, blank=False)
	featured = models.BooleanField(default=False)
	new = models.BooleanField(default=True)
	articleOfTheWeek = models.BooleanField(default=False)
	active = models.BooleanField(default=True)
	createdOn = models.DateTimeField(default=timezone.now)
	slug = models.SlugField(editable=False, unique=True, default='')

	def __str__(self):
		return  f"{self.title} - {self.author}"

	def get_absolute_url(self):
		return reverse('article_detail', kwargs={'slug': self.slug})