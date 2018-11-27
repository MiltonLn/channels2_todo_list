from django.urls import path, include

urlpatterns = [
    path('', include('lists.urls', namespace='lists')),
]
