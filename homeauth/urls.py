from django.urls import path
from homeauth.views import views
app_name = 'homeauth'
urlpatterns = [
    path('signup', views.signUp, name='signup'),
    path('login', views.logIn, name='login'),
    path('logout', views.logOut, name='logout'),
]
