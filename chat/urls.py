from django.urls import path
from chat import views
from django.contrib.auth import views as auth_views

app_name = 'chat'

urlpatterns = [
    path('', views.index, name = 'home'),
    path('signup/', views.signup, name = 'signup'),
    path('login/', auth_views.LoginView.as_view(template_name = 'chat/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]