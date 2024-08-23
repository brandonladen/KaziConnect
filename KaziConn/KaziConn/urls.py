from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('supper-admin/', admin.site.urls),
    path('user_account/', include('user_account.urls')),
    path('accounts/', include('allauth.urls')),
    
    
]

