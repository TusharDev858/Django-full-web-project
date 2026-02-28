from django.urls import path, include
from users import views as users_views
from django.contrib.auth import views as auth_views
from . import views


urlpatterns = [
    path('register/', users_views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', views.manual_logout, name='manual_logout'),
]