from django.urls import path
from .views import ping_async, ping_sync, ping_async_io, ping_sync_io

urlpatterns = [
    path('ping-async/', ping_async),
    path('ping-sync/', ping_sync),
    path('ping-sync-io/', ping_sync_io),
    path('ping-async-io/', ping_async_io),
]
