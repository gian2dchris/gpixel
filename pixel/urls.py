from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('pixel/', views.pixel, name='pixel'),
    #path("<tracking_url>/", views.tracking_url, name="tracking_url"),
    path('register/', views.register, name='register'),
    path('login/', views.login_req, name='login'),
    path('logout/', views.logout_req, name='logout'),
]
