from django.urls import path
from . import views
urlpatterns = [
 path('login/', views.auth_view, name='register'),
 path('login/', views.auth_view, name='login'),
 path('logout/', views.logoutuser, name='logoutuser'),
]