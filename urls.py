from django.contrib import admin
from django.urls import path

from blog import views

#Задание1
urlpatterns = [
    path('admin/', admin.site.urls),

    path('', views.user_index, name='user_index'),
]