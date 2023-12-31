"""
URL configuration for website1 project.

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
from django.urls import path
from website1 import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('aboutus/',views.AboutUs, name='about'),
    path('contactus/',views.Contact, name='contact'),
    path('blog/',views.blogs, name='blog'),
    path('blog/<slug>',views.Open_blogs, name='openblog'),
    path('videos/',views.videos, name='videos'),
    path('calculator/',views.Calculator, name='calculator'),
    path('',views.Home, name='home'),
    path('admin-panel/',views.admin_panel, name='admin-panel'),
    path('admin_login/', views.admin_login, name='admin_login'),
    path('edit-service/',views.EditService, name='edit-service'),
    path('notification_page/<slug>', views.Notify, name='notify'),
    path('aboutus/',views.AboutUs),
    path('notes/',views.Notes, name='notes'),
]

# Serve media files during development
if not settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
