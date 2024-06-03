"""dbms_project URL Configuration

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
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.HomePage,name="HomePage"),

    path('showParticipant',views.showpart,name="showpart"),
    path('Insertpart',views.Insertpart,name="Insertpart"),
    path('Edit/<int:id>',views.Editpart,name="Editpart"),
    path('Update/<int:id>',views.updatepart,name="updatepart"),
    path('Delete/<int:id>',views.Delpart,name="Delpart"),
    path('Sort',views.sortParticipant,name="sortParticipant"),
    path('runQuerypart',views.runQuerypart,name="runQuerypart"),

    path('showHackathon',views.showhack,name="showhack"),
    path('Inserthack',views.Inserthack,name="Inserthack"),
    path('Edit2/<int:id>',views.Edithack,name="Edithack"),
    path('Update2/<int:id>',views.updatehack,name="updatehack"),
    path('Delete2/<int:id>',views.Delhack,name="Delhack"),
    path('Sort2',views.sortHackathon,name="sortHackathon"),
]
