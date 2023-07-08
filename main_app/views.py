from django.shortcuts import render
from django.views import View # <- View class to handle requests
from django.http import HttpResponse # <- a class to handle sending a type of response
from django.views.generic.base import TemplateView
from .models import Player
from django.views.generic.edit import CreateView
from django.views.generic import DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
# Create your views here.


class Home(TemplateView):
    template_name = "home.html"

class About(View):
    def get(self, request):
        return HttpResponse("Basketball About")
    
class Players:
    def __init__(self, name, image, bio):
        self.name = name
        self.image = image
        self.bio = bio


players = [
  Player("Lebron James", "https://lalweb.blob.core.windows.net/public/lakers/product-marketing/web/player-page/2022-2023/2223_PlayerImage_James_1920x2304.jpg",
          "Back for his 20th NBA season, LeBron James is returning for his fifth dance with the Lakers. King James is the only player in the NBA to have won Finals MVP with three different franchises. The 4x MVP and 18x All-Star sits at No. 2 on the All-Time Scoring List."),
  Player("AD",
          "https://cdn.nba.com/teams/uploads/sites/1610612747/2022/12/GettyImages-1446793221.jpg", "Anthony Marshon Davis Jr. (born March 11, 1993) is an American professional basketball player for the Los Angeles Lakers of the National Basketball Association (NBA)."),
  Player("Stephen Curry",
          "https://media.cnn.com/api/v1/images/stellar/prod/220611102335-steph-curry-finals-game-4.jpg?c=16x9&q=h_720,w_1280,c_fill", "Wardell Stephen Curry II  born March 14, 1988)[1] is an American professional basketball player for the Golden State Warriors of the National Basketball Association (NBA)."),
]



class PlayerList(TemplateView):
    template_name = "player_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["players"] = Player.objects.all() 
        return context
    
class PlayerCreate(CreateView):
    model = Player
    fields = ['name', 'img', 'bio', 'verified_player']
    template_name = "player_create.html"
    success_url = "/players/"

class PlayerDetail(DetailView):
    model = Player
    template_name = "player_detail.html"

class PlayerUpdate(UpdateView):
    model = Player
    fields = ['name', 'img', 'bio', 'verified_player']
    template_name = "player_update.html"
    success_url = "/players/"

class PlayerDelete(DeleteView):
    model = Player
    template_name = "players_delete_confirmation.html"
    success_url = "/players/"