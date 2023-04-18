from django.shortcuts import render, redirect

from renting_wbscp.forms import UserForm
from renting_wbscp.web_scraper import buy_place, house_renting, buy_terrain
from django.views.generic import View


# Create your views here.

class SignUpView(View):
    def get(self, request):
        form_user = UserForm()
        return render(request, 'signup.html', {"form": form_user})

    def post(self, request):
        form_user = UserForm(request.POST)
        if form_user.is_valid():
            user = form_user.save()
            user.refresh_from_db()
            user.save()
            return redirect('index')


class ContactView(View):
    def get(self, request):
        return render(request, 'contact.html')


class AboutView(View):
    def get(self, request):
        return render(request, 'about.html')

class ExploreView(View):
    def get(self, request):
        return render(request, 'explore.html')

class ScrapPlacesView(View):
    def get(self, request):
        return render(request, 'rent_houses.html')


class UserDataView(View):
    def get(self, request):
        return render(request, 'contact.html')


# class BuyPlace(View):
#     def get(self, request):
#         return render(request, 'buy_places.html')
#
#     def post(self, request):
#         list_of_places = None
#         min_budget = request.POST.get('min_budget')
#         max_budget = request.POST.get('max_budget')
#
#         if min_budget == '' and max_budget == '':
#             list_of_places = buy_place(0, 100000000000)
#         if min_budget == '' and max_budget != '':
#             list_of_places = buy_place(0, max_budget)
#         if min_budget != '' and max_budget == '':
#             list_of_places = buy_place(min_budget, 100000000000)
#         if min_budget != '' and max_budget != '':
#             list_of_places = buy_place(min_budget, max_budget)
#
#         context = {
#             "list": list_of_places,
#         }
#         return render(request, 'buy_places.html', context=context)


class BuyPlaces(View):
    def get(self, request):
        return render(request, 'buy_places.html')

    def post(self, request):
        list_of_places = None
        min_budget = request.POST.get('min_budget')
        max_budget = request.POST.get('max_budget')

        if min_budget == '' and max_budget == '':
            list_of_places = buy_place(0, 100000000000)
        if min_budget == '' and max_budget != '':
            list_of_places = buy_place(0, max_budget)
        if min_budget != '' and max_budget == '':
            list_of_places = buy_place(min_budget, 100000000000)
        if min_budget != '' and max_budget != '':
            list_of_places = buy_place(min_budget, max_budget)

        context = {
            "list": list_of_places,
        }
        return render(request, 'buy_places.html', context=context)


class RentTerrainsView(View):
    def get(self, request):
        return render(request, 'rent_terrains.html')

    def post(self, request):
        list_of_terrains = None

        min_budget = request.POST.get('min_budget')
        max_budget = request.POST.get('max_budget')

        if min_budget == '' and max_budget == '':
            list_of_terrains = buy_terrain(0, 100000000000)
        if min_budget == '' and max_budget != '':
            list_of_terrains = buy_terrain(0, max_budget)
        if max_budget == '' and min_budget != '':
            list_of_terrains = buy_terrain(min_budget, 100000000000)
        if min_budget != '' and max_budget != '':
            list_of_terrains = buy_terrain(min_budget, max_budget)

        context = {
            "list": list_of_terrains,
        }

        return render(request, 'rent_terrains.html', context=context)


class RentHousesViews(View):
    def get(self, request):
        return render(request, 'rent_houses.html')

    def post(self, request):
        list_of_houses = None
        if request.method == "POST":
            min_budget = request.POST['min_budget']
            max_budget = request.POST['max_budget']

            if min_budget == '' and max_budget == '':
                list_of_houses = house_renting(0, 100000000000)
            if min_budget == '' and max_budget != '':
                list_of_houses = house_renting(0, max_budget)
            if min_budget != '' and max_budget == '':
                list_of_houses = house_renting(min_budget, 100000000000)
            if min_budget != '' and max_budget != '':
                list_of_houses = house_renting(min_budget, max_budget)

            context = {
                "list": list_of_houses,
            }

            return render(request, 'rent_houses.html', context=context)

