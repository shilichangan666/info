from django.urls import path
from Book.views import index,goods,shops,register,json,response,jsonresponse,redirectresponse
urlpatterns = [
    path('index/',index),
    path('<cat_id>/<id>/',goods),
    path('<city_id>/<shop_id>/',shops),
    path('register/',register),
    path('json/',json),
    path('res',response),
    path('jsonresponse/',jsonresponse),
    path('redirect/',redirectresponse)

]