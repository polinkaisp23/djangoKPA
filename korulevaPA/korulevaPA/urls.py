from django.contrib import admin
from django.urls import path
from mainKPA import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', views.RegFunc),
    path('main/', views.mainFunc),
]
