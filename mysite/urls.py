from django.contrib import admin
from django.urls import path
from myBotVK.views import index as bot

urlpatterns = [
    path('admin/', admin.site.urls),
    path('botVK/', bot)
]