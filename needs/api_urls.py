from django.urls import path
from django.conf.urls import url
from needs import views_api

from django.conf.urls.static import static
from django.conf import settings


urlpatterns=[
    path('need/', views_api.needApi),
    path('need/<int:id>',views_api.needApi),
    path('needByUserId/<int:id>',views_api.getNeedByUserId),
    path('needByOfferId/<int:id>',views_api.getNeedByOfferId),



]
