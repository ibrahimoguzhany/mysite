from django.contrib import admin
from django.urls import path, include
from users import views as user_views
from django.contrib.auth import views as authentication_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('food/', include('food.urls')),
    path('register', user_views.register, name='register'),
    path('login/',authentication_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/',authentication_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
]