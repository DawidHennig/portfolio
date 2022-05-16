from django.shortcuts import render
from django.views import View
from app.models import Donation, Institution

# Create your views here.


class LandingPage(View):

    def get(self, request):
        context = {}
        context['bags_quantity'] = sum([x.quantity for x in Donation.objects.all()])   
        context['institution_quantity'] = len(Institution.objects.all())   
        context['fundacje'] = Institution.objects.filter(i_type=1)
        context['pozarządowe'] = Institution.objects.filter(i_type=2)
        context['zbiórki'] = Institution.objects.filter(i_type=3)
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
