"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from vege import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns



urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.recipie),
    path('delete-recipie/<int:id>/',views.delete_recipie,name='delete-recipie'),
    path('update-recipie/<id>', views.update,name='update-recipie'),
    path('login/',views.login_page,name='login'),
    path('register/',views.register,name='register'),
    path('logout_page/',views.logout_page,name='logout_page')

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
