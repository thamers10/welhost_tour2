from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('signup/', views.signup_view, name='signup'),
    path('logout/', views.logout_view, name='logout'),
    path('guides/', views.guide_list, name='guide_list'),
    path('drivers/', views.driver_list, name='driver_list'),
]
