from django.urls import path
from temp_app import views

urlpatterns= [
    path('',views.home),
    path('register',views.register),
    path('login',views.login),
    path('userhome',views.userhome),
    path('edit',views.edit),
    path('mygallery',views.mygallery),
    path('logout',views.logout),
    path('image',views.image),
    path('audio',views.audio),
    path('video',views.video),
]