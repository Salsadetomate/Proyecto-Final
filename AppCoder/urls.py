from django.urls import path
from AppCoder import views


urlpatterns = [
    path('', views.Introduccion),
    path("sobremi", views.sobremi),

    

]