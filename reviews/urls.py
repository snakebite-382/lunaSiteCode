from django.urls import path

from .views import(
	ReviewPostsListView,
	ReviewPostDetailView,

	ReviewPostDeleteView,
	ReviewPostUpdateView
	)

urlpatterns = [
	path('', ReviewPostsListView.as_view(), name="review-list"),
	path('<slug:slug>/', ReviewPostDetailView.as_view(), name='review-detail'),
	path('<slug:slug>/delete', ReviewPostDeleteView.as_view(), name='review-delete'),
	path('<slug:slug>/update', ReviewPostUpdateView.as_view(), name='review-update'),
]