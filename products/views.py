from django.shortcuts import render
from .models import Product

from django.http import Http404
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



def single(request,slug):
    print(slug)
    try:
        product = Product.objects.get(slug=slug)
        context = {'product':product}
        template = 'single.html'
        return render(request,template,context)
    except:
        raise Http404
 