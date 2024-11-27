from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('user/<str:username>/', views.user_profile, name='user_profile'),
    path('post/<int:post_id>/', views.post_detail, name='post_detail'),
]
