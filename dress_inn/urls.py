from django.urls import path

import views

app_name = "dress_inn"

urlpatterns = [
    path('diesel', views.scrape_diesel, name="scrape_diesel")
]
