import datetime

from django.http import JsonResponse, HttpResponse
from django.views.decorators.http import require_GET, require_POST, require_http_methods
from django.utils import timezone
import json

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from .models import UserQuery
from .serializers import *
from . import address_checker

# Create your views here.

'''
# 1st version works for backend
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

# from django.views.decorators.csrf import csrf_exempt

# @require_POST
# @csrf_exempt
@require_http_methods(["GET", "POST"]) # Temporarily available for GET.
def add_query(request):
    if request.method == "GET":
        query = request.GET.get("query", None)
        if query:
            json_obj = {
                "query": query,
                "query_date": timezone.now()
            }
            return JsonResponse(json_obj)
        return HttpResponse(status=400)

    elif request.method == "POST":
        # data = request.POST.get("data", None) # Only works for form
        data = request.body.decode("utf-8")     # Works for Json
        data = json.loads(data)
        if data:
            query = data.get("query")
            query_date = timezone.now()
            q = UserQuery(query=query, query_date=query_date)
            q.save()
            return HttpResponse("Query Added!", status=201)
        
        return HttpResponse(status=400)

    else:
        return HttpResponse(status=405)
'''

'''
# 2nd version works for non table web demo
@api_view(['GET', 'POST'])
def init_db(request):
    if request.method == 'GET':
        data = UserQuery.objects.all()

        serializer = UserQuerySerializer(data, context={'request': request}, many=True)

        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = UserQuerySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
            
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT', 'DELETE'])
def index(request, pk):
    try:
        homes = UserQuery.objects.get(pk=pk)
    except UserQuery.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        serializer = UserQuerySerializer(homes, data=request.data,context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        homes.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
'''

@api_view(['GET', 'POST'])
def history(request):
    if request.method == 'GET':
        data = UserQuery.objects.all()

        serializer = UserQuerySerializer(data, context={'request': request}, many=True)

        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = UserQuerySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
            
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT', 'DELETE'])
def search(request, pk):
    try:
        homes = UserQuery.objects.get(pk=pk)
    except UserQuery.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        serializer = UserQuerySerializer(homes, data=request.data,context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        homes.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)