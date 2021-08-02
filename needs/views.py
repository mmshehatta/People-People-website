from needs.models import Need
from django.contrib.auth.models import User
from django.http.response import HttpResponse, JsonResponse
from offers.forms import OfferForm
from django.shortcuts import render,redirect

from offers.models import Category, Offer

from django.core.files.storage import default_storage

from django.core.paginator import Paginator

from .filters import OfferFilter

from django.core.paginator import Paginator

# import django_filters

# import sweetify

from django.contrib import messages

from django.template.loader import render_to_string

from django.contrib.auth.decorators import login_required




#********************* user needs list view************
def user_needs(request):
    # needs = Need.objects.all()
    needs = Need.objects.filter(borrower=request.user)
    print("N"*40)
    print(needs)
    context = {
        'needs':needs
    }
  
    return render(request , 'pages/needs/user_needs.html',context)

#********************* user needs list view************
def add_need(request):
    if request.method =="GET" and request.is_ajax():
        id2 = request.GET['offer_id']
        new_offer = Offer.objects.get(id=id2)
        new_need = Need()
        new_need.offer = new_offer
        new_need.borrower = request.user
        new_need.save()
        return HttpResponse("success")
    else:
        return HttpResponse("Request Method is not GET")




#********************* need_delete view************
def need_delete(request,id):
    need_by_id = Need.objects.get(id=id)
    if request.method =="GET" and request.is_ajax():
        need_by_id.delete()
    data = {
            "obj":str(need_by_id)
        }
    return JsonResponse(data, safe=False)