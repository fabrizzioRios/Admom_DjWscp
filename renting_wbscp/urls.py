from django.urls import path

from renting_wbscp.views import SignUpView, ExploreView, AboutView, BuyPlaces, RentTerrainsView, RentHousesViews, UserDataView, ContactView
from django.contrib.auth.views import LoginView, LogoutView


urlpatterns = [
    path('', LoginView.as_view(template_name="index.html"), name="index"),
    path('signup/', SignUpView.as_view(), name="signup"),
    path('explore/', ExploreView.as_view(), name="explore"),
    path('about/', AboutView.as_view(), name="about"),
    path('buy-place/', BuyPlaces.as_view(), name="place"),
    path('rent-terrains/', RentTerrainsView.as_view(), name="terrains"),
    path('rent-houses/', RentHousesViews.as_view(), name="houses"),
    path('my-profile/', UserDataView.as_view(), name="profile"),
    path('contact/', ContactView.as_view(), name="contact"),
    path('logout/', LogoutView.as_view(), name="logout"),
]
