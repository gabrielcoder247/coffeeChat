from django.contrib import admin
from django.urls import path,include
from justchat.views import index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('chat/', include('justchat.urls', namespace = 'chat')),
]
