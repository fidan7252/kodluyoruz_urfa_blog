from django.contrib import admin
from django.urls import path
from blog import views as blog_views
from blog_user import views as blog_user_views

urlpatterns = [
    path('', blog_views.index, name='home'),
    path('login/', blog_user_views.login_user, name='login'),
    path('logout/', blog_user_views.logout_user, name='logout'),
    path('signup/', blog_user_views.sign_up, name='signup'),
    path('category/<slug:cat_slug>/', blog_views.index, name='cat'),
    path('category/<slug:cat_slug>/<slug:post_slug>/', blog_views.post_detail, name='post_detail'),
    path('admin/', admin.site.urls),
]

