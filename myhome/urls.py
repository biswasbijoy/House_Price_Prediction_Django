"""
URL configuration for myhome project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls import static
from predict import urls as predict_urls
from posts import urls as posts_url
from homeauth import urls as homeauth_urls
from chat import urls as chat_urls

app_name = 'myhome'
urlpatterns = [
                  path('admin/', admin.site.urls),
                  # path('', views.start, name='start'),
                  # path('home', views.home, name='home'),
                  # path('login', views.login, name='login'),
                  path('', include(predict_urls, namespace='predict')),
                  path('', include(posts_url, namespace='posts')),
                  path('', include(homeauth_urls, namespace='homeauth')),
                  path('', include(chat_urls, namespace='chats')),
              ] + static.static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
