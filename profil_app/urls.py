from django.urls import path
from profil_app import views

urlpatterns = [
    path('profiles', views.ProfileList.as_view()),
]
