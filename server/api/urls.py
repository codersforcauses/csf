"""
URL configuration for api project.

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
from .actions import export2csv

admin.site.add_action(export2csv, "csv_export_selected")

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/team/", include("api.team.urls")),
    path("api/event/", include("api.event.urls")),
    path("api/auth/", include("api.auth.urls")),
    path("api/mileage/", include("api.mileage.urls")),
    path("api/subteam/", include("api.subteam.urls")),
    path("api/user/", include("api.users.urls")),
]
