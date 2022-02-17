#base app specific url
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('category/<str:pk>/', views.category, name="category"),
    path('create-category', views.createCategory, name="create-category"),
    path('update-category/<str:pk>/', views.updateCategory, name="update-category"),
    path('delete-category/<str:pk>/', views.deleteCategory, name="delete-category"),

]