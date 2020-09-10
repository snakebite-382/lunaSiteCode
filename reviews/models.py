from django.db import models
from django.urls import reverse
from django.utils import timezone

# Create your models here.
class Review(models.Model):
	product = models.CharField(max_length=120)
	author = models.CharField(max_length=120, default="Anonymous")


	STAR_CHOICES = (
		('1S','1 star'),
		('2S', "2 star"),
		("3S", "3 star"),
		("4S", "4 star"),
		("5S", "5 star")
	)
	rating = models.CharField(
			max_length=120,
			choices=STAR_CHOICES,
			default="1 star"
		)

	body = models.TextField()
	featured = models.BooleanField(default=False)
	active = models.BooleanField(default=True)
	createdOn = models.DateTimeField(default=timezone.now)

	def get_absolute_url(self):
		return reverse("review-detail", kwargs={"id": self.id})

	def __str__(self):
		return f"{self.product} - {self.rating} - {self.author}"