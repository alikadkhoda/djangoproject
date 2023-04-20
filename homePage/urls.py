from django.urls import path
from homePage import views

urlpatterns = [
    path('', views.indexView, name='index'),
    path('projects',views.projectView)
]