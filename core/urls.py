
from django.urls import path

from core.views import frontpage, privacy, terms, plans

urlpatterns = [
    path('', frontpage, name='frontpage'),
    path('privacy/', privacy, name='privacy'),
    path('terms/', terms, name='terms'),
    path('plans/', plans, name='plans'),
]