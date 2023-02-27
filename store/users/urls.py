from django.urls import path

from .views import login, registration, logout, profile

app_name = 'users'

urlpatterns = [
    path('login/', login, name='login'),
    path('register/', registration, name='register'),
    path('logout/', logout, name='logout'),
    path('profile/', profile, name='profile'),
]