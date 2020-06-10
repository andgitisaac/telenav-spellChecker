import datetime

# from django.http import JsonResponse, HttpResponse
# from django.views.decorators.http import require_GET, require_POST, require_http_methods
# from django.utils import timezone
import json

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from .models import UserQuery
from .serializers import *
from . import address_checker

# Create your views here.

@api_view(["DELETE"])
def delete(request):
    import pdb; pdb.set_trace()
    return

@api_view(["GET"])
def history(request):
    # import pdb; pdb.set_trace()
    if (request.method == "GET"):
        data = UserQuery.objects.all()
        serializer = UserQuerySerializer(data, context={'request': request}, many=True)
        return Response(serializer.data)

    # elif (request.mehtod == 'DELETE'):
    #     print('Deleting history')
    #     import pdb; pdb.set_trace()

@api_view(["POST"])
def add_query(request):
    serializer = UserQuerySerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(status=status.HTTP_201_CREATED)
        
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(["POST"])
def search(request):
    data = request.body.decode("utf-8")
    data = json.loads(data)
    if data:
        query = data.get("query")
        outputs = address_checker.corrections(query)        

        json_data = json.dumps(outputs)
        return Response(json_data)
    
    content = {"Message": "Empty body"}
    return Response(content, status=status.HTTP_400_BAD_REQUEST)
        
