from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render
from django.views import View
from app.models import Donation, Institution, User, Category
from django.shortcuts import redirect
from django.db.models import Sum
from app.forms import RegisterForm, LoginForm
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.


class LandingPage(View):

    def get(self, request):
        context = {}
        context['bags_quantity'] = Donation.objects.all().aggregate(Sum('quantity'))['quantity__sum'] 
        context['institution_quantity'] = Institution.objects.all().count()
        context['fundations'] = Institution.objects.filter(i_type=1)
        context['nongovernmental'] = Institution.objects.filter(i_type=2)
        context['fundraiser'] = Institution.objects.filter(i_type=3)
        return render(request, "index.html", context)


class AddDonation(LoginRequiredMixin, View):
    login_url = '/login/'

    def get(self, request):
        context = {}
        context['categories'] = Category.objects.all()
        context['institutions'] = Institution.objects.all()
        return render(request, "form.html", context)


class Login(View):

    def get(self, request):
        form = LoginForm()
        return render(request, "login.html", {"form": form})

    def post(self, request):
        form = LoginForm(request.POST) 
        if form.is_valid():
            email = form.cleaned_data['email'] 
            password = form.cleaned_data['password'] 
            user = authenticate(request, email=email, password=password)
            if user:
                login(request, user)
                return redirect("index") 
        return redirect("register") 


class Logout(View):
    def get(self, request):
        logout(request)
        return redirect('index')


class Register(View):

    def get(self, request):
        form = RegisterForm()
        return render(request, "register.html", {"form": form})

    def post(self, request):
        form = RegisterForm(request.POST) 
        if form.is_valid():
            name = form.cleaned_data['name'] 
            surname = form.cleaned_data['surname'] 
            email = form.cleaned_data['email'] 
            password = form.cleaned_data['password'] 
            password2 = form.cleaned_data['password2'] 
            User.objects.create_user(email=email, password=password, first_name=name, last_name=surname)
            return redirect("login") 
        return redirect("register") 
