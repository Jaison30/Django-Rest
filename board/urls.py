"""scrum URL Configuration

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

from django.conf.urls import url,include
from rest_framework import routers

from .views import *

router = routers.DefaultRouter()
router.register(r'sprint', SprintViewSet, base_name='sprint')
router.register(r'task', TaskViewSet, base_name='task')
router.register(r'users', UserViewSet, base_name='UserViewSet')


#router.register(r'tokens/<key>/', UserTokenAPIView, base_name='tokens')


urlpatterns = [
    url(r'^login$', UserLoginAPIView.as_view(), name="login"),
    url('tokens/<key>/', UserTokenAPIView.as_view(), name="token"),
]

