from . import views
from django.urls import path

urlpatterns = [
    path('',views.myindex,name='index'),
    path('submitquery',views.submitquery,name='submitquery'),
]