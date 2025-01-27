from django.shortcuts import render

# Create your views here.
def home (request):
    return render(request, 'home.html')
def formget(request): 
    if request.GET.get('btn'):
        a=request.GET.get('n')
        b=request.GET.get('a')
        c=request.GET.get('e')
        d=request.GET.get('p')
        return render(request,'formget.html',{'name':a,'age':b,'email':c,'password':d})
    return render(request, 'formget.html')


def formpost(request):
    if request.method=='POST':
        a=request.POST.get('n')
        b=request.POST.get('a')
        c=request.POST.get('e')
        d=request.POST.get('p')
        return render(request,'formpost.html',{'name':a,'age':b,'email':c,'password':d})
    return render(request, 'formpost.html')


#GET - http method 
#get - variable value to use get 