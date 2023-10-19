
from django.urls import path
from django.contrib.auth import views as auth_views

from core.views import frontpage, privacy, terms, plans, signup

urlpatterns = [
    path('', frontpage, name='frontpage'),
    path('privacy/', privacy, name='privacy'),
    path('terms/', terms, name='terms'),
    path('plans/', plans, name='plans'),

    path('signup/', signup, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='core/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]