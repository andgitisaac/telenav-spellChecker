import datetime

from django.http import JsonResponse, HttpResponse
from django.views.decorators.http import require_GET, require_POST, require_http_methods
from django.utils import timezone

from .models import UserQuery


# Create your views here.

@require_POST
def init_db(request):
    test_cases = [
        ['774 Miller Spurs Apt. 077 Maxwellshire, SC 63480', datetime.datetime(2020, 4, 6, 0, 10, 9, tzinfo=timezone.utc)],
        ['5572 John Place Apt. 013 South Corey, CA 49091', datetime.datetime(2020, 3, 20, 7, 21, 26, tzinfo=timezone.utc)],
        ['Unit 5248 Box 1246 DPO AP 14956', datetime.datetime(2020, 3, 29, 18, 7, 47, tzinfo=timezone.utc)],
        ['312 Hall Tunnel Mariamouth, WY 25861', datetime.datetime(2020, 3, 21, 23, 11, 39, tzinfo=timezone.utc)],
        ['PSC 1657, Box 2317 APO AE 83648', datetime.datetime(2020, 3, 17, 14, 13, 3, tzinfo=timezone.utc)],
        ['USNS Phillips FPO AP 58550', datetime.datetime(2020, 3, 24, 10, 12, 29, tzinfo=timezone.utc)],
        ['3722 Jessica Unions Suite 038 Murrayshire, GA 62388', datetime.datetime(2020, 4, 2, 9, 26, 13, tzinfo=timezone.utc)],
        ['4323 Henson Manor Stacyside, AR 34615', datetime.datetime(2020, 3, 29, 10, 40, 15, tzinfo=timezone.utc)],
        ['960 Victoria Plaza Suite 170 South Lori, IN 23855', datetime.datetime(2020, 3, 15, 8, 52, 39, tzinfo=timezone.utc)],
        ['28966 Patricia Isle Patriciabury, NY 04869', datetime.datetime(2020, 3, 20, 4, 8, 44, tzinfo=timezone.utc)],
        ['327 Jackson Greens Apt. 568 Debramouth, TX 66805', datetime.datetime(2020, 3, 30, 21, 18, 3, tzinfo=timezone.utc)],
        ['404 Schmitt Squares Lake Debraborough, SD 57178', datetime.datetime(2020, 3, 26, 22, 9, 56, tzinfo=timezone.utc)],
        ['Unit 6470 Box 1097 DPO AA 24578', datetime.datetime(2020, 4, 1, 15, 4, 50, tzinfo=timezone.utc)]
    ]
    
    for query, time in test_cases:
        q = UserQuery(query=query, query_date=time)
        q.save()
    return HttpResponse("Initialized!")


@require_GET
def index(request):

    latest_queries = UserQuery.objects.order_by("query_date")
    queries = []
    for q in latest_queries:
        queries.append({
            "query": q.query,
            "query_date": q.query_date
        })

    json_obj = {"queries": queries}
    return JsonResponse(json_obj)


@require_POST
def add_query(request):
    data = request.POST.get("data", None)
    if data:
        query = data.get("query")
        query_date = timezone.now()
        q = UserQuery(query=query, query_date=query_date)
        q.save()
        return HttpResponse(status=201)
    
    return HttpResponse(status=400)