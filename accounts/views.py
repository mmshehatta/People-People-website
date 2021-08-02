from offers.models import Offer
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect, render
from .forms import P_info_form, SignUpForm, U_info_form
from django.contrib.auth.decorators import login_required

from .models import Profile

from django.contrib import messages

# Create your views here.


def signUp(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            # to make signup user is loged in
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username , password=password)
            login(request , user)
            return redirect('home')
    else:
         form = SignUpForm()
    return render(request , "pages/account/signup.html" , {'form':form})




@login_required
def profile(request , user):
    offer_list = Offer.objects.order_by('-id').all()

    print(type(user))
    print("#-#"*30)
    print(request.path[18:23])
    print("*$#" * 30)
    profile = Profile.objects.get(user=user)
    print("*$" * 30)
    print(profile)
    print("*" * 30)
    if request.method == "POST":
      u_info_form = U_info_form(request.POST,  instance=request.user)
      p_info_form = P_info_form(request.POST ,request.FILES , instance=profile)
      if u_info_form.is_valid() and p_info_form.is_valid():
          u_info_form.save()
          myprofile = p_info_form.save(commit=False)
          myprofile.user = request.user    
          myprofile.save()
          messages.success(request , f"Your Profile Updated Succefully!")

    else:
        u_info_form = U_info_form(instance=request.user)
        p_info_form = P_info_form(instance=profile)
        
    context ={
        'user_info_form':u_info_form,
        'profile_info_form':p_info_form,
        'profile':profile,
        'url':int(request.path[18:23]),
        'offers':offer_list,
        'title':'profile'
    }

    return render(request , 'pages/account/profile.html',context)