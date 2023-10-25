from django.urls import path
from .views import CarListAPIView, RegisterView, LoginView, UserView, LogoutView

urlpatterns =[
    path('cars/', CarListAPIView.as_view(), name='car-list'),
    path('register', RegisterView.as_view()),
    path('login', LoginView.as_view()),
    path('user', UserView.as_view()),
    path('logout', LogoutView.as_view()),

]