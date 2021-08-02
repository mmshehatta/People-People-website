from accounts.models import Profile
from needs.models import Need
from django.contrib.auth.models import User
from django.http.response import JsonResponse
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

import pyttsx3


# Create your views here.

# *************************** Home Page View ***********************
def home(request):
    # engine = pyttsx3.init()
    # engine.say(f"Hi ,  {request.user} , in , our , Web , site")
    # engine.setProperty('rate',200000) 
    # engine.runAndWait()
    offer_list = Offer.objects.order_by('-id').all()
    myfilter = OfferFilter(request.GET,queryset= offer_list )
    filltered_offers = myfilter.qs

    paginator = Paginator(filltered_offers, 3) # Show 3 contacts per page.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)



    context = {
        'offers' : page_obj,
        'myfilter':myfilter,
        # 'profile' : Profile.objects.get(user=request.user)
    }
    return render(request , 'pages/home.html', context)

# *************************** /end Home Page View ***********************

# *************************** get_offer_list View ***********************
def get_offer_list(request):
    # engine = pyttsx3.init()
    # engine.say(f"Hi , {request.user} , you will ,  find   , all  ,   avaulable Offers ,  here! ")
    # engine.setProperty('rate',200000) 
    # engine.runAndWait()
    offer_list = Offer.objects.order_by('-id').all()
    # offer_list = Offer.objects.filter(status='available')

    # filler library
    # myfilter = OfferFilter(request.GET,queryset= offer_list )
    # filltered_offers = myfilter.qs

    #paginator
    paginator = Paginator(offer_list, 3) # Show 3 contacts per page.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
        'offers' : page_obj,       
        'title':'home'

    }
    return render(request , 'pages/offers/offers.html', context)
# *************************** /get_offer_list View ***********************


# *************************** Add offer View ***********************

def add_offer(request):
    # engine = pyttsx3.init()
   
    if request.method == "POST":
        form =  OfferForm(request.POST , request.FILES)
        if form.is_valid():
            myform = form.save(commit=False)
            myform.owner = request.user
            myform.save()
            messages.success(request, f' Congratulations ,Your Offer has been Added Successfully! ')
            # engine.say(f" Congrats ,Your , Offer,  has ,  been ,  Added ,  Successfully! ")
            # engine.setProperty('rate',2) 
            # engine.runAndWait()
            return redirect('offers_list')
    else:
          form = OfferForm()

    context={
         'form':form,
    }

    return render(request , 'pages/offers/add_offer.html', context)
    


# *************************** /end Add offer View ***********************




#********************* offer_update view************

def offer_update(request,id):

    offer_by_id = Offer.objects.get(id=id)
    if request.method =="POST":
        offer_update_form = OfferForm(request.POST , request.FILES , instance=offer_by_id)
        if offer_update_form.is_valid():
            offer_update_form.save()
            messages.success(request , 'offer Updated Successfully')
            return redirect('offers_list')
    else:
        offer_update_form = OfferForm(instance=offer_by_id)

    context={
            'form':offer_update_form
        }
    return render(request ,'pages/offers/offer_update.html',context)

#********************* offer_delete view************
def offer_delete(request,id):
    offer_by_id = Offer.objects.get(id=id)
    if request.method =="GET" and request.is_ajax():
        offer_by_id.delete()
        return redirect('offers_list')
    # data = {
    #         "obj":str(offer_by_id)
    #     }
    # return JsonResponse(data)

    return render(request ,'pages/offers/offer_delete.html')

#********************* offer_details view************
@login_required
def offer_details(request ,id):
    offer_by_id = Offer.objects.get(id=id)
    contxt={
        'offer': offer_by_id
    }
    return render(request ,'pages/offers/offer_details.html' , contxt)


#********************* offer_search_view************
def offer_search_page(request):
    return render(request ,'pages/offers/offer_search.html')


def offer_search_view(request):
    searched_offers = Offer.objects.all()
    ctx = {}
    url_parameter = None
    if 'search_name' in request.GET:
        url_parameter = request.GET['search_name']
        if url_parameter:
            searched_offers = searched_offers.filter(name__icontains=url_parameter)
        else:
            searched_offers = Offer.objects.all()
        ctx["searched_offers"] = searched_offers

        if request.is_ajax():
            html = render_to_string(
                template_name="pages/offers/offer_search.html",
                context={"searched_offers": searched_offers}
            )

            data_dict = {"html_from_view": html}

            return JsonResponse(data=data_dict, safe=False)


    return render(request ,'pages/offers/offer_search.html' ,context=ctx)
    # if request.is_ajax():
    #     res = None
    #     offer = request.GET.get('offer')
    #     qs = Offer.objects.filter(name__icontains=offer)
    #     if len(qs) > 0 and len(offer) > 0 :
    #         data=[]
    #         for pos in qs:
    #             item={
    #                 'pk':pos.pk,
    #                 'name':pos.name,
    #                 'description':pos.description,
    #                 'image':str(pos.image),
    #                 'place':pos.place,
    #                 'date':pos.date,
    #                 'phone':pos.phone,
    #                 'status':str(pos.status),
    #                 'owner' : str(pos.owner),
    #                 'category':str(pos.category)

    #             }
    #             data.append(item)
    #         res=data
    #     else:
    #         res = "No offer Found"
    #     print(offer)
    #     return JsonResponse({'data':res})
    # return JsonResponse({})





#********************* user_offers view************
def user_offers(request):
    # engine = pyttsx3.init()
    # engine.say(f"Hi , {request.user} , you will ,  find all your ,  offers here")
    # engine.setProperty('rate',2) 
    # engine.runAndWait()
    offers = Offer.objects.filter(owner = request.user)

    context = {
        'offers':offers
    }

    return render(request , 'pages/offers/user_offers.html',context)



