from django.urls import path
from Book.views import index,goods,shops,register,json,response,jsonresponse,\
    redirectresponse,cookie,cookieread,delcookie,set_session,get_session
urlpatterns = [
    path('index/',index),
    path('<cat_id>/<id>/',goods),
    path('<city_id>/<shop_id>/',shops),
    path('register/',register),
    path('json/',json),
    path('res',response),
    path('jsonresponse/',jsonresponse),
    path('redirect/',redirectresponse),
    path('cookie/',cookie),
    path('cookies/',cookieread),
    path('delcookie/',delcookie),
    path('set_session/',set_session),
    path('get_session/',get_session)

]