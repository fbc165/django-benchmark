from django.http import JsonResponse
import asyncio
import time

async def ping_async_io(request):
    await asyncio.sleep(1)
    return JsonResponse({'message': 'pong-async-io'})

def ping_sync_io(request):
    time.sleep(1)
    return JsonResponse({'message': 'pong-sync-io'})

async def ping_async(request):
    return JsonResponse({'message': 'pong-async'})

def ping_sync(request):
    return JsonResponse({'message': 'pong-sync'})