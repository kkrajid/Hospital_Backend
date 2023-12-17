
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('api/admins/', admin.site.urls),
    path('api/', include('accounts.urls'), name='api_root'),
]

