
from django.urls import path
from account.views import *
urlpatterns = [
    path('register/',UserRegistrationView.as_view(),name="register"),
    path('login/',userLoginView.as_view(),name="login"),
    path('profile/',UserProfileView.as_view(),name="profile"),
    path('changepass/',UserChangePasswordView.as_view(),name="changepass"),
    
]
