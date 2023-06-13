from django.urls import re_path
from buysell import views
from django.urls import path, include
from .views import  login
from django.views.decorators.csrf import csrf_exempt

from buysell.models import SmsStats
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
# router.register(r'savedUserState', views.ProfileWithCurrentStateViewset)

urlpatterns = [

    path('', include(router.urls)),
    path('api/login', login),
    re_path(r'^api/register', csrf_exempt(views.CreateUserView.as_view())),

    re_path(r'^api/profile/', views.profile),


    re_path(r'^api/getWazirxData$', views.getWazirxData),
    re_path(r'^api/getHistoricalData/', views.getHistoricalData),

]