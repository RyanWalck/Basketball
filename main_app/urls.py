from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name="home"),
    path('about/', views.About.as_view(), name="about"),
    path('players/', views.PlayerList.as_view(), name="player_list"),
    path('players/new/', views.PlayerCreate.as_view(), name="plater_create"),
    path('players/<int:pk>/', views.PlayerDetail.as_view(), name="player_detail"),
    path('players/<int:pk>/update',views.PlayerUpdate.as_view(), name="player_update"),
    path('players/<int:pk>/delete',views.PlayerDelete.as_view(), name="player_delete"),
]
