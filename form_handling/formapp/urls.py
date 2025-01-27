from django.urls import path 
from.import views
urlpatterns=[
    path('',views.home),
    path('formget',views.formget),
    path('formpost',views.formpost),
             ]