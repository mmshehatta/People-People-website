from django.urls import path
from django.conf.urls import url
from offers import views

from django.conf.urls.static import static
from django.conf import settings


urlpatterns=[
    path('category/', views.categoryApi),
    path('category/<int:id>',views.categoryApi),
    path('offer/', views.offerApi),
    path('offer/<int:id>',views.offerApi),
    path('offerd/<int:id>',views.offerApiId),
    path('offerid/<int:id>',views.offerApibyId),
    path('offerByOfferId/<int:id>',views.offerApibyOfferId),
    path('offerByuserId/<int:id>',views.offerByUserId),
    path('categoryById/<int:id>',views.getCatById),
    path('offerSearch/<str:name>',views.offerSearch),

   





    


    # categoryById


    # path('SaveFile', views.SaveFile),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
