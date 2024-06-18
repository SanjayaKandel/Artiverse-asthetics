
from django.urls import path
from . import views

urlpatterns = [
    # path('<int:id>/', views.artwork_detail, name='artwork_detail'),
    path('create/', views.artwork_create, name='artwork_create'),
    path('<int:id>/update/', views.artwork_update, name='artwork_update'),
    path('<int:id>/delete/', views.artwork_delete, name='artwork_delete'),
]