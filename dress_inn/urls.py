from django.urls import path

from . import views

app_name = "dress_inn"

urlpatterns = [
    path('diesel', views.scrape_diesel, name="scrape_diesel")
]
