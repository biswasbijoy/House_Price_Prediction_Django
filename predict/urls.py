from django.urls import path
from predict.views import views

app_name = 'predict'
urlpatterns = [
    path('prediction.html', views.prediction, name='predict'),
    path('predict', views.prediction_result, name='prediction_result'),
    path('ehehbouy', views.location, name='ehehbouy'),
]
