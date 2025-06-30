"""
URL configuration for Ticketing_System project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from user_panel import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', auth_views.LoginView.as_view(template_name='main/login.html'), name = 'login'),
    path('register/', views.register_view, name='register'),
    path('user_panel/', include('user_panel.urls')),
    path('user/', views.user, name = "user"),
    path('ticket_creation/', views.ticket_creation_view, name='ticket_creation'),
    path('user_tickets/', views.user_tickets_view, name='user_tickets'),
    path('delete_ticket/<int:ticket_id>/', views.delete_ticket_view, name='delete_ticket'),
    path('update_ticket/<int:ticket_id>/', views.update_ticket_view, name='edit_ticket'),

]
