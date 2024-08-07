from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('choose-template/', views.choose_template, name='choose_template'),
    path('purchase-template/<int:template_id>/', views.purchase_template, name='purchase_template'),
    path('store/<str:store_name>/', views.store_view, name='store_view'),
]