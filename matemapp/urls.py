from django.urls import path
from .views import main, savollar
urlpatterns = [
    path('', main, name='main'),
    path('post/<int:id>/', savollar, name='savollar'),
]