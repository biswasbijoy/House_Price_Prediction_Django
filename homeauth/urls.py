from django.urls import path
from homeauth.views import views
from homeauth.views.views import PasswordsChangeView

app_name = 'homeauth'
urlpatterns = [
    path('signup', views.signUp, name='signup'),
    path('login', views.logIn, name='login'),
    path('logout', views.logOut, name='logout'),
    path('edit-profile', views.EditProfilePageView.as_view(), name='edit_profile'),
    path('<int:pk>/password/', PasswordsChangeView.as_view(), name='password'),
]
