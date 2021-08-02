from django.urls import path
from django.conf.urls import url
from followup import views

from django.conf.urls.static import static
from django.conf import settings


urlpatterns=[
    path('question/', views.questionApi),
    path('question/<int:id>',views.questionApi),

    path('contactus/', views.contactusApi),
    path('contactus/<int:id>',views.contactusApi),

    path('review/', views.reviewApi),
    path('review/<int:id>',views.reviewApi),

    # path('SaveFile', views.SaveFile),
]