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
			articleOfTheWeek = Article.objects.filter(articleOfTheWeek="True", active="True")
			# if len(articleOfTheWeek) > 1:
			# 	articleOfTheWeek = article_of_the_week[0]
			# 	print("multiple articles of the week")
			print("AOW: ")
			print(articleOfTheWeek[0])
			print("Blog ")
			print(querysetFeaturedArticles[0])
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