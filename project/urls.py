
from django.urls import path

from .views import ( projects, project, edit_project, task, edit_task, edit_entry,
                     delete_entry, delete_untracked_entry, track_entry )


# Url pattern

app_name = 'project'

urlpatterns = [
    path('', projects, name='projects'),
    path('<int:project_id>/', project, name='project'),
    path('<int:project_id>/<int:task_id>/', task, name='task'),
    path('<int:project_id>/<int:task_id>/edit/', edit_task, name='edit_task'),
    path('<int:project_id>/<int:task_id>/<int:entry_id>/edit/', edit_entry, name='edit_entry'),
    path('<int:project_id>/<int:task_id>/<int:entry_id>/delete/', delete_entry, name='delete_entry'),
    path('<int:project_id>/edit/', edit_project, name='edit_project'),
    path('delete_untracked_entry/<int:entry_id>/', delete_untracked_entry, name='delete_untracked_entry'),
    path('track_entry/<int:entry_id>/', track_entry, name='track_entry'),
]