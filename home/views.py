from django.shortcuts import render

from django.views import View

from blog.models import Article
from reviews.models import Review

# Create your views here.
class HomePageView(View):
	template_name = "index.html"
	def get(self, request, *args, **kwargs):
		try:
			querysetNew = Article.objects.filter(new="True", active="True")
			querysetFeaturedArticles = Article.objects.filter(featured="True", active="True")
			querysetFeaturedReviews =  Review.objects.filter(featured="True", active="True")
			articleOfTheWeek = Article.objects.get(articleOfTheWeek="True", active="True")
			context = {
				"object_list_new": querysetNew,
				"object_list_featured_articles": querysetFeaturedArticles,
				"object_list_featured_reviews": querysetFeaturedReviews,
				"article_of_the_week": articleOfTheWeek,
			}
		except Exception as e:
			print(e)
			context = {}
		return render(request, self.template_name, context)