from django.urls import path
from Book.views import index
urlpatterns = [
    path('index/',index)
]