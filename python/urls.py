from django.urls import path
from . import views
urlpatterns = [
    path("", views.index, name="index"),
    path("calculate/", views.calculate_average, name="calculate_average"),
]