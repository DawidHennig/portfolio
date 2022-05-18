from django.shortcuts import render
from django.views import View
from app.models import Donation, Institution, EmailUser
from django.shortcuts import redirect
from django.contrib.auth.models import User

# Create your views here.


class LandingPage(View):

    def get(self, request):
        context = {}
        context['bags_quantity'] = sum([x.quantity for x in Donation.objects.all()])   
        context['institution_quantity'] = len(Institution.objects.all())   
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
        EmailUser.objects.create_user(username=name+"_"+surname, first_name=name, last_name=surname, email=email, password=password)

        return redirect('login') 
