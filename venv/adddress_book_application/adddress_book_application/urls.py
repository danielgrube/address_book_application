"""adddress_book_application URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.conf.urls import url
from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from address_book_application.core import views as core_views
from django.comf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path(r'^login/$', auth_views.login, {'template_name': 'core/login.html'}, name='login'),
    path(r'^logout/$', auth_views.logout, {'template_name': 'logged_out.html'}, name='logout'),
    path(r'^create_contact/$', core_views.create_contact, name='create_contact'),
    path(r'admin/', admin.site.urls),
    path(r'^user/', include('address_book_application.urls')),
    path(r'^admin/', include(admin.site.urls)),
    path(r'profile/(?P<username>[a-zA-A0-9]+)$', views.get_user_profile),
    path(r'^del_user/(?P<username>[a-zA-A0-9]+)$', 'profile.views.del_user'),
]
