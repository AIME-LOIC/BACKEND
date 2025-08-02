from django.urls import path
from . import views  # or from myapp import views

urlpatterns = [
    path('home/', views.home, name='home'),  # example
]
