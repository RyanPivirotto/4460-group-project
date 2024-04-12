from django.urls import path
from .views import DramaList, DramaDetails, ActorList, DirectorList, HomepageView, DramaAdd, DramaDelete, DramaEdit #LoginView
from . import views

urlpatterns = [
    path('drama/', DramaList.as_view(), name='drama-list'),
    path('dramas/<int:id>/', DramaDetails.as_view(), name='drama-details'),
    path('drama/<int:id>/edit', views.DramaEdit.as_view(), name='drama-edit'),
    path('directors/', DirectorList.as_view(), name='director-list'),
    path('add/', DramaAdd.as_view(), name='drama-add'),
    path('delete/', DramaDelete.as_view(), name='drama-delete'),
    path('edit/', DramaEdit.as_view(), name='drama-edit'),
    path('actors/', ActorList.as_view(), name='actor-list'),
    path('actor/add', views.ActorAdd.as_view(), name='actor-add'),
    path('actor/<int:id>/update/', views.ActorUpdate.as_view(), name='actor-update'),
    path('actor/<int:id>/delete/', views.ActorDelete.as_view(), name='actor-delete'),
    #path('login/', LoginView.as_view(), name = 'login'),
    path('homepage/', HomepageView.as_view(), name = 'homepage'),
    # Add more URL patterns for other views if needed
]
