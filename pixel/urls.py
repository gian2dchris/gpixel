from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('pixel/', views.pixel, name='pixel'),
    path('settings/', views.settings, name='settngs'),
    path("pixel/<tracking_slug>/", views.pixel, name="tracking_slug"),
    path('register/', views.register, name='register'),
    path('login/', views.login_req, name='login'),
    path('logout/', views.logout_req, name='logout'),
]
