from likes import views
from django.urls import path
urlpatterns = [
    path('likes/',views.LikeList.as_view()),
    path('likes/<int:pk>/', views.LikeDetails.as_view())

]