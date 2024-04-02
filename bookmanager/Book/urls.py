from django.urls import path
from Book.views import index,shops,register,json
urlpatterns = [
    path('index/',index),
    # path('<cat_id>/<id>/',goods),
    path('<city_id>/<shop_id>/',shops),
    path('register/',register),
    path('json/',json),

]