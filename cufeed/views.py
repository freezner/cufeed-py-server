from django.http import JsonResponse
from cufeed.service.FeedService import FeedService
from dotenv import load_dotenv

load_dotenv(".env", verbose=True)


# 헬스 체크
def health_check(request):
    return JsonResponse(status=200, data={'status': 'true', 'message': 'OK'})


# 뉴스 수집
def collect_news(request, vendor, keyword):
    feed_service = FeedService()

    if feed_service.collect_feeds(vendor=vendor, keyword=keyword):
        return JsonResponse(status=200, data={'status': 'true', 'message': 'OK'})