from django.urls import path
from offers import views



urlpatterns=[
    path('offers' , views.get_offer_list , name='offers_list'),
    path('add-new-offer' , views.add_offer , name='add_offer' ),
    path('<int:id>/update' , views.offer_update , name='update' ),
    path('<int:id>/delete' , views.offer_delete , name='delete' ),
    path('<int:id>' , views.offer_details , name='offer_details' ),
    path('search-page' , views.offer_search_page , name='search_page' ),
    path('search' , views.offer_search_view , name='offer_search' ),
    path('user-offers' , views.user_offers , name='user_offers' ),
    
    ]
