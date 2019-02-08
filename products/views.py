from django.shortcuts import render

# Create your views here.
def home(request):
    template = 'base.html'
    if request.user.is_authenticated:
        context = {"username":request.user,"email":request.user.email}
    else:
        context = {"username":request.user,"email":""} #request.user.email does not exist

    return render(request,template,context)

