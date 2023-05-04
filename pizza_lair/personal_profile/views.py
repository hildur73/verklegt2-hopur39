from django.shortcuts import render
from personal_profile.models import User

# Create your views here.
def index(request):
    context = {'personal_profile:': User.objects.all()}
    return render(request, 'personal_profile/index.html', context)