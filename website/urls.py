from django.urls import path
from website import views

urlpatterns = [
  path('', views.home, name='home'),
  path('mail/', views.mail, name='mail'),
  path('logout/', views.logout_user, name='logout'),
  path('register/', views.register, name='register')
]