from django.urls import path
from predict.views import views

app_name = 'predict'
urlpatterns = [
    path('predict', views.prediction, name='predict'),
]
