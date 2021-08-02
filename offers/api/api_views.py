from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from offers.models import Category, Offer
from offers.serializers import CategorySerializer, OfferSerializer

from django.core.files.storage import default_storage

from django.core.paginator import Paginator

from .filters import OfferFilter

from django.core.paginator import Paginator

import django_filters


# Create your views here.


def home(request):
    offer_list = Offer.objects.all()
    myfilter = OfferFilter(request.GET,queryset= offer_list )
    filltered_offers = myfilter.qs

    paginator = Paginator(filltered_offers, 3) # Show 3 contacts per page.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)


    
    context = {
        'offers' : page_obj,
        'myfilter':myfilter
    }
    return render(request , 'pages/home.html', context)








# ########################### categoryApi #################


@csrf_exempt
def categoryApi(request, id=0):
    if request.method == 'GET':
        categorys = Category.objects.all()
        categorys_serializer = CategorySerializer(categorys, many=True)
        return JsonResponse(categorys_serializer.data, safe=False)

    elif request.method == 'POST':
        category_data = JSONParser().parse(request)
        category_serializer = CategorySerializer(data=category_data)
        if category_serializer.is_valid():
            category_serializer.save()
            return JsonResponse("Added SuccessFully!!", safe=False)
        return JsonResponse("Failed to Add", safe=False)

    elif request.method == 'PUT':
        category_data = JSONParser().parse(request)
        category = Category.objects.get(id=category_data['id'])
        category_serializer = CategorySerializer(category, data=category_data)
        if category_serializer.is_valid():
            category_serializer.save()
            return JsonResponse("Updated Successfully !!", safe=False)
        return JsonResponse("Failed to Update", safe=False)

    elif request.method == 'DELETE':
        category = Category.objects.get(id=id)
        category.delete()
        return JsonResponse("Deleted Successfully", safe=False)


@csrf_exempt
def getCatById(request, id):
    if request.method == 'GET':
        category = Category.objects.get(id=id)
        categorys_serializer = CategorySerializer(category)
        return JsonResponse(categorys_serializer.data, safe=False)

# ########################### offerApi #################


@csrf_exempt
def offerApi(request, id=0):
    if request.method == 'GET':
        offers = Offer.objects.all().order_by('id')
        paginator = Paginator(offers, 3) # Show 3 offers per page.
        page_number = request.GET.get('page',1)
        page_obj = paginator.get_page(page_number)
        # print('((((((((((((((( page_number)))))))))))))))))))))',  page_number)
        # print('(((((((((((((((page_obj)))))))))))))))))))))', page_obj)
        # print('(((((((((((((((page_obj.has_previous)))))))))))))))))))))',page_obj.has_next)


        offers_serializer = OfferSerializer(offers, many=True)
        # print('(((((((((((((((offers_serializer)))))))))))))))))))))', offers_serializer)

        return JsonResponse(offers_serializer.data, safe=False)

    elif request.method == 'POST':
        offer_data = JSONParser().parse(request)
        offer_serializer = OfferSerializer(data=offer_data)
        if offer_serializer.is_valid():
            offer_serializer.save()
            return JsonResponse("Added SuccessFully!!", safe=False)
        return JsonResponse("Failed to Add", safe=False)

    elif request.method == 'PUT':
        offer_data = JSONParser().parse(request)
        offer = Offer.objects.get(id=offer_data['id'])
        offer_serializer = OfferSerializer(offer, data=offer_data)
        if offer_serializer.is_valid():
            offer_serializer.save()
            return JsonResponse("Updated Successfully !!", safe=False)
        return JsonResponse("Failed to Update", safe=False)

    elif request.method == 'DELETE':
        offer = Offer.objects.get(id=id)
        offer.delete()
        return JsonResponse("Deleted Successfully", safe=False)


@csrf_exempt
def offerApiId(request, id=0):
    if request.method == 'GET':
        offers = Offer.objects.filter(Cat_id=id)
        offers_serializer = OfferSerializer(offers, many=True)
        return JsonResponse(offers_serializer.data, safe=False)


@csrf_exempt
def offerApibyId(request, id=0):
    if request.method == 'GET':
        offers = Offer.objects.get(id=id)
        offers_serializer = OfferSerializer(offers)
        return JsonResponse(offers_serializer.data, safe=False)


@csrf_exempt
def offerApibyOfferId(request, id=0):
    if request.method == 'GET':
        offers = Offer.objects.filter(id=id)
        offers_serializer = OfferSerializer(offers,  many=True)
        return JsonResponse(offers_serializer.data, safe=False)


@csrf_exempt
def offerByUserId(request, id=0):
    if request.method == 'GET':
        offers = Offer.objects.filter(user_id=id)
        offers_serializer = OfferSerializer(offers, many=True)
        return JsonResponse(offers_serializer.data, safe=False)


@csrf_exempt
def offerSearch(request, name):
    if request.method == 'GET':
        offers = Offer.objects.filter(name=name)
        offers_serializer = OfferSerializer(offers, many=True)
        return JsonResponse(offers_serializer.data, safe=False)
