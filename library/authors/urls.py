from django.urls import path
from . import views

urlpatterns = [
    path('authors/', views.AuthorListCreate.as_view(), name='author-list-create'),
    path('authors/<int:pk>/', views.AuthorDetail.as_view(), name='author-detail'),
]
