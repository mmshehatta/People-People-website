from django.urls import path
from django.conf.urls import url
from needs import  views

from django.conf.urls.static import static
from django.conf import settings


urlpatterns=[
       path('user-needs' , views.user_needs , name='user_needs' ),
       path('add-new-need' , views.add_need , name='add_need' ),
       path('<int:id>/delete/need' , views.need_delete , name='need_delete' ),

]
