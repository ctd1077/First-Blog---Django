from django.conf.urls import url
from django.urls import path
from .views import HomeBlogView, BlogDetailView
 
urlpatterns = [  
    path('post/<int:pk>/', BlogDetailView.as_view(), name='post_detail'),
    path('', HomeBlogView.as_view(), name='home'),
]