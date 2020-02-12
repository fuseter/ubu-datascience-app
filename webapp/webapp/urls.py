from django.contrib import admin
from django.urls import path
from houseapp import views as houseapp
urlpatterns = [
    path('', houseapp.index),
    path('admin/', admin.site.urls),
]
