from django.http import JsonResponse
import redis
from django.conf import settings

def health_check(request):
    r = redis.Redis.from_url(settings.REDIS_URL)
    r.set("last_check", "ok")
    return JsonResponse({
        "status": "ok",
        "redis": r.get("last_check").decode()
    })