from django.shortcuts import render, get_object_or_404, redirect
from django.views import View

from django.views.generic import ListView, DetailView

from .models import Article
from .forms import ArticleCreateForm

class GetObjectMixin(object):
	model = Article
	slug = 'slug'

	def get_object(self):
		slug= self.kwargs.get(self.slug)
		obj = None
		if slug is not None:
			obj = get_object_or_404(self.model, slug=slug)
		return obj


# Create your views here.

#Admin Article management
class BlogPostCreateView(View):
	template_name = "blog/create.html"

	def get(self, request, *args, **kwargs):
		form = ArticleCreateForm()
		context = {
			'form': form
		}
		return render(request, self.template_name, context)

	def post(self, request, *args, **kwargs):
		form = ArticleCreateForm(request.POST)
		if form.is_valid():
			form.save()
			form = ArticleCreateForm()
		context = {
			'form': form
		}
		return render(request, self.template_name, context)

class BlogPostDeleteView(GetObjectMixin, View):
	template_name = "blog/delete.html"

	def get(self, request, pk=None, *args, **kwargs):
		context = {
			"obj": self.get_object()
		}
		return render(request, self.template_name, context)

	def post(self, request, id=None, *args ,**kwargs):
		obj = self.get_object()
		context = {}

		if obj is not None:
			obj.delete()
			context['obj'] = None
			return redirect('/blog')

		return render(request, self.template_name, context)

class BlogPostUpdateView(GetObjectMixin, View):
	template_name = 'blog/update.html'

	def get(self, request, *args, **kwargs):
		context = {}
		obj = self.get_object()

		if obj is not None:
			form = ArticleCreateForm(instance=obj)
			context['obj'] = obj
			context['form'] = form

		return render(request, self.template_name, context)

	def post(self, request, *args, **kwargs):
		obj = self.get_object()
		context = {}
		form = ArticleCreateForm(request.POST)

		if obj is not None:
			form = ArticleCreateForm(request.POST, instance=obj)
			if form.is_valid():
				form.save()
				return redirect(obj.get_absolute_url())
			context['obj'] = obj
			context['form'] = form


		return render(request, self.template_name, context)


# User Article viewing
class BlogPostsListView(View):
	template_name = "blog/index.html"

	def get(self, request, *args, **kwargs):

		querysetAll = Article.objects.filter(active="True").order_by("-id")

		try:
			querysetNew = Article.objects.filter(new="True", active="True").order_by("-id")
		except:
			querysetNew = Article.objects.get(new="True", active="True").order_by("-id")

		try:
			querysetFeatured = Article.objects.filter(featured="True", active="True").order_by("-id")
		except:
			querysetFeatured = Article.objects.get(featured="True", active="True").order_by("-id")


		context = {
			"object_list_all": querysetAll,
			"object_list_new": querysetNew,
			"object_list_featured": querysetFeatured
		}

		return render(request, self.template_name, context)

class BlogPostDetailView(DetailView):
    model = Article
    template_name = 'blog/detail.html'