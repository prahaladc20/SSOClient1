"""SSOClient1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.http.response import HttpResponse
from simple_sso.sso_client.client import Client
from django.contrib.auth.views import LoginView

from django.conf import settings
from SSOClient1 import settings

test_client = Client(settings.SSO_SERVER, settings.SSO_PUBLIC_KEY, settings.SSO_PRIVATE_KEY)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^client/', include(test_client.get_urls())),
    url('^$', lambda request: HttpResponse('home' + str(request.user)), name='root')

]
