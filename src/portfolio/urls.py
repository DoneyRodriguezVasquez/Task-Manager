from django.urls import path 
from .views import (
    portfolio,facturacion,whappip,wiki,marketing,landing
) 

app_name = 'portfolio'

urlpatterns = [
    path('portfolio/', portfolio, name='portfolio'),
    path('facturacion/', facturacion, name='facturacion'),
    path('whappip/', whappip, name='whappip'),
    path('wiki/', wiki, name='wiki'),
    path('marketing/', marketing, name='marketing'),
    path('landing/', landing, name='landing'),

]