from django.urls import path, include
from .views import (
    home,
    about,
    page_list,
    page_detail,
    page_create,
    page_update,
    page_delete,
)


urlpatterns = [
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('pages/', page_list, name='page_list'),
    path('pages/<int:pk>/', page_detail, name='page_detail'),
    path('pages/create/', page_create, name='page_create'),
    path('pages/update/<int:pk>/', page_update, name='page_update'),
    path('pages/delete/<int:pk>/', page_delete, name='page_delete'),
]