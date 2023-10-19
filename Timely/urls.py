
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    ## Core App
    path('', include('core.urls')),

    ## Dashboard App
    path('dashboard/', include('dashboard.urls')),
]
