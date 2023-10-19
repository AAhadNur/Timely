
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    ## Core App
    path('', include('core.urls')),

    ## User App
    path('myaccount/', include('user.urls')),

    ## Team App
    path('team/', include('team.urls')),

    ## Project App
    path('project/', include('project.urls')),
]
