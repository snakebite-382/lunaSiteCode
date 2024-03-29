from django.contrib import admin
from django.urls import path, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from pages.views import contact_view, about_view
from home.views import HomePageView

from pages import views as page_views

urlpatterns = [
    path('blog/', include('blog.urls')),
    path('reviews/', include('reviews.urls')),

    path('admin/', admin.site.urls),

	path('',HomePageView.as_view()),
    path('contact/', contact_view, name='contact'),
    path('about/', about_view, name='about'),

]