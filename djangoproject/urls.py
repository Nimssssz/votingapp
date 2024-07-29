
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('', include('rootapp.urls')),
    path('admin/', admin.site.urls),
    path('votingapp', include('votingapp.urls')),
]