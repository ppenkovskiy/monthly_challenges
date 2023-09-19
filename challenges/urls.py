from django.urls import path
from . import views

urlpatterns = [
    path('january', views.index_1),
    path('february', views.index_2)
]