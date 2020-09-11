from django.urls import path

from .views import(
	BlogPostsListView,
	BlogPostDetailView,
	BlogPostDeleteView,
	BlogPostUpdateView
	)

urlpatterns = [
	path('', BlogPostsListView.as_view(), name="blog-list"),
	path('<slug:slug>/', BlogPostDetailView.as_view(), name='blog-detail'),
	path('<slug:slug>/delete', BlogPostDeleteView.as_view(), name='blog-delete'),
	path('<slug:slug>/update', BlogPostUpdateView.as_view(), name='blog-update'),
]