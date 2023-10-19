

from django.urls import path, include

from .views import dashboard, view_user

#

urlpatterns = [
    path('', dashboard, name='dashboard'),
    path('<int:user_id>/', view_user, name='view_user'),

    # Project App
    path('projects/', include('project.urls')),

    # User App
    path('myaccount/', include('user.urls')),

    # Team App
    path('myaccount/teams/', include('team.urls')),
]