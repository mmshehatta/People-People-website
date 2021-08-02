from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from needs.models import Need
from needs.serializers import NeedSerializer

from django.core.files.storage import default_storage

# Create your views here.

@csrf_exempt
def needApi(request,id=0):
    if request.method=='GET':
        needs = Need.objects.all()
        needs_serializer = NeedSerializer(needs, many=True)
        return JsonResponse(needs_serializer.data, safe=False)
    
    elif request.method=='POST':
        need_data=JSONParser().parse(request)
        need_serializer = NeedSerializer(data=need_data)
        if need_serializer.is_valid():
            need_serializer.save()
            return JsonResponse("Added SuccessFully!!", safe=False)
        return JsonResponse("Failed to Add", safe=False)
    
    elif request.method == 'PUT':
        need_data = JSONParser().parse(request)
        need=Need.objects.get(id=need_data['id'])
        need_serializer=NeedSerializer(need, data=need_data)
        if need_serializer.is_valid():
            need_serializer.save()
            return JsonResponse("Updated Successfully !!", safe=False)
        return JsonResponse("Failed to Update", safe=False)

    elif request.method=='DELETE':
        need=Need.objects.get(id=id)
        need.delete()
        return JsonResponse("Deleted Successfully", safe=False)




@csrf_exempt
def getNeedByUserId(request,id=0):
    if request.method=='GET':
       needs = Need.objects.filter(user_id=id)
       needs_serializer = NeedSerializer(needs, many=True)
       return JsonResponse(needs_serializer.data, safe=False)


@csrf_exempt
def getNeedByOfferId(request,id=0):
    if request.method=='GET':
       needs = Need.objects.filter(offer_id=id)
       needs_serializer = NeedSerializer(needs, many=True)
       return JsonResponse(needs_serializer.data, safe=False)
