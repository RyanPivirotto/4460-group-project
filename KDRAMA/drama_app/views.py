from django.shortcuts import render, redirect
from django.urls import reverse
from .models import Award, Character, Director, Drama, Actor, User
from django.views import View
from .forms import DirectorForm, DramaForm, ActorForm, AwardForm, CharacterForm
from django.contrib.auth import authenticate #login
from django.contrib import messages
from .serializers import DramaSerializer 
from rest_framework import generics


# Create your views here.
        
class DramaList(generics.ListCreateAPIView):
    serializer_class = DramaSerializer
    def get(self,request):
        drama = Drama.objects.all()
        return render(request=request, template_name='drama/drama_list.html',context={'drama':drama})
     
class DramaDetails(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = DramaSerializer
    def get(self,request,id):
        drama = Drama.objects.get(pk=id)
        return render(request=request, template_name='drama/drama_detail.html',context={'drama':drama})

class ActorList(View):
    def get(self,request):
        actor = Actor.objects.all()
        return render(request=request, template_name='drama/actor_list.html',context={'actor':actor})

class DirectorList(View):
    def get(self,request):
        director = Director.objects.all()
        return render(request=request, template_name='drama/director_list.html',context={'director':director})

class LoginView(View):
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
    
############################
# CRUD Operations for User #
############################
class UserAdd(View):
    def get(self,request):

        user = User.objects.all()

        return redirect('login')

class UserUpdate(View):

    def get(self,request,user_id=None):
        if user_id:
            user = User.objects.get(pk=user_id)
        else:
            user = User()

        return render(request, 'homepage.html')
    
    def post(self,request,user_id=None):

        if user_id:
            user = User.objects.get(pk=user_id)
        else:
            user = User()
        
        return render(request, 'homepage.html')
    
class UserDelete(View):

    def get(self,request,user_id=None):

        if user_id:
            user = User.objects.get(pk=user_id)
        else:
            user = User()

        return render(request, 'homepage.html')
      
    
    def post(self,request,user_id=None):

        user = User.objects.get(pk=user_id)

        user.delete()

        return render(request, 'homepage.html')