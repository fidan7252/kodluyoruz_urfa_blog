from django.contrib import admin
from django.urls import path
from blog import views as blog_views

urlpatterns = [
    path('', blog_views.index, name='home'),
    path('category/<slug:cat_slug>/', blog_views.index, name='cat'),
    path('category/<slug:cat_slug>/<slug:post_slug>/', blog_views.post_detail, name='post_detail'),
    path('admin/', admin.site.urls),
]

