from django.urls import path
from .views import GenerateRandomUserView


urlpatterns = [
    path("", GenerateRandomUserView.as_view()),
]

