from django.shortcuts import render
from .models import Product

# Create your views here.
def home(request):
    template = 'base.html'
    if request.user.is_authenticated:
        context = {"username":request.user,"email":request.user.email}
    else:
        context = {"username":request.user,"email":""} #request.user.email does not exist

    return render(request,template,context)


def all(request):
    context = {'products':Product.objects.all()}
    template = 'all.html'

    return render(request,template,context)