from django.urls import path
from . import views
# from sili.views import home, get_response

urlpatterns = [
    path('', views.main,  name='main'),
]