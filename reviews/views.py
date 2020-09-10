from django.shortcuts import render, get_object_or_404, redirect
from django.views import View

from .models import Review
from .forms import ReviewCreateForm

class GetObjectMixin(object):
	model = Review
	id = 'id'

	def get_object(self):
		id = self.kwargs.get(self.id)
		obj = None
		if id is not None:
			obj = get_object_or_404(self.model, id=id)
		return obj


# Create your views here.

#Admin Article management
class ReviewPostCreateView(View):
	template_name = "reviews/create.html"

	def get(self, request, *args, **kwargs):
		form = ReviewCreateForm()
		context = {
			'form': form
		}
		return render(request, self.template_name, context)

	def post(self, request, *args, **kwargs):
		form = ReviewCreateForm(request.POST)
		if form.is_valid():
			form.save()
			form = ReviewCreateForm()
		context = {
			'form': form
		}
		return render(request, self.template_name, context)

class ReviewPostDeleteView(GetObjectMixin, View):
	template_name = "reviews/delete.html"

	def get(self, request, id=None, *args, **kwargs):
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
			return redirect('/reviews')

		return render(request, self.template_name, context)

class ReviewPostUpdateView(GetObjectMixin, View):
	template_name = 'reviews/update.html'

	def get(self, request, *args, **kwargs):
		context = {}
		obj = self.get_object()

		if obj is not None:
			form = ReviewCreateForm(instance=obj)
			context['obj'] = obj
			context['form'] = form

		return render(request, self.template_name, context)

	def post(self, request, *args, **kwargs):
		obj = self.get_object()
		context = {}
		form = ReviewCreateForm(request.POST)

		if obj is not None:
			form = ReviewCreateForm(request.POST, instance=obj)
			if form.is_valid():
				form.save()
				return redirect(obj.get_absolute_url())
			context['obj'] = obj
			context['form'] = form


		return render(request, self.template_name, context)


# User Article viewing
class ReviewPostsListView(View):
	template_name = "reviews/index.html"

	def get(self, request, *args, **kwargs):
		querysetAll = Review.objects.all()
		querysetFeatured = Review.objects.filter(featured="True")
		context = {
			"object_list_all": querysetAll,
			"object_list_featured": querysetFeatured
		}

		return render(request, self.template_name, context)

class ReviewPostDetailView(GetObjectMixin, View):
	template_name="reviews/detail.html"

	def get(self, request, id=None,*args, **kwargs):
		context = {
			"obj": self.get_object()
		}

		return render(request, self.template_name, context) 