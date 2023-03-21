from django.urls import path

from renting_wbscp.views import explore_view, about_view, contact_view, signup_view, user_data_view
from django.contrib.auth.views import LoginView, LogoutView


urlpatterns = [
    path('', LoginView.as_view(template_name="index.html"), name="index"),
    path('signup/', signup_view, name="signup"),
    path('explore/', explore_view, name="explore"),
    path('about/', about_view, name="about"),
    path('my-profile/', user_data_view, name="profile"),
    path('contact/', contact_view, name="contact"),
    path('logout/', LogoutView.as_view(), name="logout"),
]
