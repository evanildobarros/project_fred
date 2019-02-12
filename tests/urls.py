from django.urls import path
from . import views
# from sili.views import home, get_response

app_name = 'sili'


urlpatterns = [
    path('', views.main,  name='main'),
    path('get-response/', views.get_response),
]