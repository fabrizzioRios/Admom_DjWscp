from django.shortcuts import render, redirect

from renting_wbscp.forms import UserForm
from renting_wbscp.web_scraper import buy_place, house_renting, buy_terrain


# Create your views here.


def contact_view(request):
    return render(request, 'contact.html')


def about_view(request):
    return render(request, 'about.html')


def explore_view(request):
    return render(request, 'explore.html')


def scrap_places_view(request):
    return render(request, 'rent_houses.html')


def user_data_view(request):
    return render(request, 'contact.html')


def buy_a_place(request):
    list_of_places = None

    if request.method == "POST":
        min_budget = request.POST['min_budget']
        max_budget = request.POST['max_budget']

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
    return render(request, 'buy_places.html')


def rent_terrains(request):
    list_of_terrains = None

    if request.method == "POST":
        min_budget = request.POST['min_budget']
        max_budget = request.POST['max_budget']

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
    else:
        return render(request, 'rent_terrains.html')


def rent_houses(request):
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
    else:
        return render(request, 'rent_houses.html')


def signup_view(request):
    if request.method == 'POST':
        form_user = UserForm(request.POST)
        if form_user.is_valid():
            user = form_user.save()
            user.refresh_from_db()
            user.save()
            return redirect('index')
    else:
        form_user = UserForm()
    return render(request, 'signup.html', {"form": form_user})
