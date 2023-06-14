
from django.urls import path
from . import views 

urlpatterns = [
    path('', views.main_page, name='home'),
    path('parse', views.parse_page, name='parse'),
    
]


""" 
from django.urls import path
from . import views

urlpatterns = [
    path('', views.run_parser_view),
]
 """