from django.contrib import admin
from django.urls import path
from blog import views as blog_views
from blog_user import views as blog_user_views

urlpatterns = [
    path('', blog_views.index, name='home'),

    #USER
    path('login/', blog_user_views.login_user, name='login'),
    path('logout/', blog_user_views.logout_user, name='logout'),
    path('signup/', blog_user_views.sign_up, name='signup'),

    # LIST    
    path('category/<slug:cat_slug>/', blog_views.index, name='cat'),
    path('category/<slug:cat_slug>/<slug:post_slug>/', blog_views.post_detail, name='post_detail'),
    
    # Category
    path('category_list/', blog_views.category_list, name='category_list'),
    path('category_list/delete/<int:category_id>/<slug:status>/', blog_views.category_update_status, name='category_delete'),
    path('add_category/', blog_views.add_category, name='add_category'),

    path('admin/', admin.site.urls),
]

