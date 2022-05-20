from django.shortcuts import render
from django.views import View
from app.models import Donation, Institution
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.db.models import Sum

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
        return render(request, "register.html")

    def post(self, request):
        name = request.POST['name'] 
        surname = request.POST['surname'] 
        email = request.POST['email'] 
        password = request.POST['password'] 
        password2 = request.POST['password2'] 
        print(name, surname, email, password, password2)
        EmailUser.objects.create_user(first_name=name, last_name=surname, email=email, password=password)

        return redirect('login') 
