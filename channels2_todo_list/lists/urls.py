from django.urls import path

from . import views

app_name = 'lists'

urlpatterns = [
    path('', views.TODOListView.as_view(), name='home'),
    path('create/', views.TODOListCreateView.as_view(), name='create'),
    path('detail/<uuid:pk>', views.TODOListDetailView.as_view(), name='detail'),
]