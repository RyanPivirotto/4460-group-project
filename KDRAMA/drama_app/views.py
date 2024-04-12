from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse, reverse_lazy
from .models import Award, Character, Director, Drama, Actor, User
from django.views import View
from .forms import DirectorForm, DramaForm, ActorForm, AwardForm, CharacterForm
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .serializers import DramaSerializer 
from rest_framework import generics


# Create your views here.        
class DramaList(generics.ListCreateAPIView):
    serializer_class = DramaSerializer
    def get(self,request):
        dramas = Drama.objects.all()
        return render(request=request, template_name='drama_list.html',context={'dramas':dramas})
     
class DramaDetails(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = DramaSerializer
    def get(self,request,id):
        drama = Drama.objects.get(pk=id)
        return render(request=request, template_name='drama_details.html',context={'drama':drama})

class ActorList(View):
    def get(self,request):
        actors = Actor.objects.all()
        return render(request=request, template_name='actor_list.html',context={'actors':actors})

class DirectorList(View):
    def get(self,request):
        directors = Director.objects.all()
        return render(request=request, template_name='director_list.html',context={'directors':directors})

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
    
##############################
# CRUD Operations for KDRAMA #
##############################
class DramaAdd(View):
    def get(self, request):
        form = DramaForm()
        return render(request=request, template_name='drama_add.html', context={'form': form})

    def post(self, request):
        form = DramaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('homepage') 
        else:
            return render(request=request, template_name='drama_add.html', context={'form': form})
        
class DramaDelete(View):
    def post(self, request, id):
        drama = get_object_or_404(Drama, id=id)
        drama.delete()
        return redirect('drama-list')
    
    def get(self, request, id):
        return render(reverse('drama-detail'))

class DramaEdit(View):
    model = Drama
    form_class = DramaForm
    template_name = 'drama_edit.html'  # Name your template appropriately
    success_url = reverse_lazy('drama-list')  # Redirect to the drama list page after a successful update

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action'] = 'Edit Drama'
        return context

#############################
# CRUD Operations for Actor #
#############################
class ActorAdd(View):
    def get(self, request):
        form = ActorForm()
        return render(request=request, template_name='actor_add.html', context={'form': form})

class ActorUpdate(View):
    model = Actor
    form_class = ActorForm
    template_name = 'actor_update.html'  
    success_url = reverse_lazy('actor-list') 

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action'] = 'Update Actor'
        return context
    
class ActorDelete(View):
    model = Actor
    success_url = reverse_lazy('actor-list') 
    template_name = 'actor_delete.html'

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