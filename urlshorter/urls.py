"""urlshorter URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path, include, reverse_lazy

from engine.forms import LoginForm, RegisterForm
from engine.views import *

accounts_urls = [
    path(
        'login/',
        LoginView.as_view(template_name="login.html", authentication_form=LoginForm),
        name='login'
    ),
    path(
        'register/',
        CreateView.as_view(     #creating a register view using django inbilt class
            template_name='register.html',
            model=User,
            form_class=RegisterForm,
            success_url=reverse_lazy('main')
        ),
        name='register'
    ),
    path(
        'logout/',
        LogoutView.as_view(template_name="logout.html"),
        name='logout'
    ),
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name="main.html"), name='main'),
    path('shorten/', ShortUrlView.as_view(), name='short_url'),
    path('links/', UserLinksView.as_view(), name='user_links_list'),
    path('link/<str:url>', UserLinkDetailView.as_view(), name='user_link_detail'),
    path('accounts/', include(accounts_urls)),
    path('<str:url>', RedirectUrlView.as_view()),
]


