from django.urls import path, include
from django.contrib import admin
urlpatterns = [
   path('star-wars/', include('api.urls')),
   path('admin/', admin.site.urls),
]