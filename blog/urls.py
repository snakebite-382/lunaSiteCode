from django.urls import path

from .views import(
	BlogPostsListView,
	BlogPostDetailView,
	BlogPostCreateView,
	BlogPostDeleteView,
	BlogPostUpdateView
	)

urlpatterns = [
	path('', BlogPostsListView.as_view(), name="blog-list"),
	path('<int:pk>/', BlogPostDetailView.as_view(), name='blog-detail'),
	path('create/', BlogPostCreateView.as_view(), name='blog-create'),
	path('<int:pk>/delete', BlogPostDeleteView.as_view(), name='blog-delete'),
	path('<int:pk>/update', BlogPostUpdateView.as_view(), name='blog-update'),
]