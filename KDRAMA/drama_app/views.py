from django.shortcuts import render, redirect
from django.urls import reverse
from .models import Award, Character, Director, Drama, Actor
from django.views import View
from .forms import DirectorForm, DramaForm, ActorForm, AwardForm, CharacterForm
from django.contrib.auth import authenticate, login
from django.contrib import messages


# Create your views here.
class DramaList(View):
    def get(self,request):
        drama = Drama.objects.all()
        return render(request=request, template_name='Drama/drama_list.html',context={'drama':drama})

class DramaDetails(View):
    def get(self,request,id):
        drama = Drama.objects.get(pk=id)
        return render(request=request, template_name='Drama/drama_detail.html',context={'drama':drama})

class ActorList(View):
    def get(self,request):
        actor = Actor.objects.all()
        return render(request=request, template_name='Drama/actor_list.html',context={'actor':actor})

class DirectorList(View):
    def get(self,request):
        director = Director.objects.all()
        return render(request=request, template_name='Drama/director_list.html',context={'director':director})

#class LoginView(View):
    def get(self, request):
        return render(request, template_name='homepage')

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('homepage')  
        else:
            messages.error(request, 'Invalid username or password')
            return redirect('login')

class HomepageView(View):
    def get(self, request):
        return render(request, 'homepage.html')