from django.urls import path
from . import views


##app_name= 'blog' ##to specify which project is going to use in the view also add 'blog:detail' in all_blogs.html

urlpatterns = [
    path('', views.all_blogs, name= 'all_blogs' ),
    path('<int:blog_id>/', views.detail, name= 'detail' ),

]