from django.shortcuts import render
from django.views import View
from app.models import Donation, Institution
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.db.models import Sum
from app.forms import RegisterForm

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


class AddDonation(View):

    def get(self, request):
        return render(request, "form.html")


class Login(View):

    def get(self, request):
        return render(request, "login.html")


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
            print(name, surname, email, password, password2)
            return redirect("login") 
        return redirect("register") 
