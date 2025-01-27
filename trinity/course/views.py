from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    name='ananya'
    college='VIT'
    # return HttpResponse('<h1> final year project </h1>') #prints message 
    return render(request, 'home.html',{'n':name,'c':college})