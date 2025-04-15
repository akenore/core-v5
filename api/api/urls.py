from django.urls import path
from . import views

app_name = 'api'

urlpatterns = [
    path('', views.APIView.as_view(), name='index'),
    
]
