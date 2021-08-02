

from .models import Profile
from django.contrib.auth.decorators import login_required

@login_required
def get_profile_data(request):
    profile_data = Profile.objects.get(user=request.user)
    return {"profile_data": profile_data}







 