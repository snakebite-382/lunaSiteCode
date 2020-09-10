from django.urls import path

from .views import( 
	ReviewPostsListView, 
	ReviewPostDetailView, 
	ReviewPostCreateView, 
	ReviewPostDeleteView,
	ReviewPostUpdateView
	)

urlpatterns = [
	path('', ReviewPostsListView.as_view(), name="review-list"),
	path('<int:id>/', ReviewPostDetailView.as_view(), name='review-detail'),
	path('create/', ReviewPostCreateView.as_view(), name='review-create'),
	path('<int:id>/delete', ReviewPostDeleteView.as_view(), name='review-delete'),
	path('<int:id>/update', ReviewPostUpdateView.as_view(), name='review-update'),
]