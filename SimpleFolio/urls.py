from django.urls import path
from .import views

urlpatterns = [
    path('', views.crypt_view, name='SimpleFolio-home'),
    path('news/', views.news_view, name='latest-news'),
    path('portfolio/', views.portf_view, name='my-portfolio'),
    path('onboarding/', views.onboarding, name='onboarding')
]