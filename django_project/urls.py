from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from users import views as user_views
from SimpleFolio.views import portf_view, portf_del

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', user_views.register, name='register'),
    path('profile/', user_views.profile, name='profile'),
    path('my-portfolio/', portf_view, name='my-portfolio'),
    path('my-portfolio/<int:id>', portf_del, name='my-portfolio-del'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('', include('SimpleFolio.urls')),
]