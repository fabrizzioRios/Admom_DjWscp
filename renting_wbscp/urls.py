from django.urls import path

from renting_wbscp.views import login, index, signup

urlpatterns = [
    path('', index, name="index"),
    path('login/', login, name="login"),
    path('signup/', signup, name="signup"),
]
