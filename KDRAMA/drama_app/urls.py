from django.urls import path
from .views import DramaList, DramaDetails, ActorList, DirectorList, HomepageView #LoginView

urlpatterns = [
    path('dramas/', DramaList.as_view(), name='drama-list'),
    path('dramas/<int:id>/', DramaDetails.as_view(), name='drama-detail'),
    path('actors/', ActorList.as_view(), name='actor-list'),
    path('directors/', DirectorList.as_view(), name='director-list'),
    #path('login/', LoginView.as_view(), name = 'login'),
    path('homepage/', HomepageView.as_view(), name = 'homepage'),
    # Add more URL patterns for other views if needed
]
