from django.shortcuts import render
from django.core.files.storage import FileSystemStorage # fss is a class that uses local stored storage
from.import dbconnection
from django.http import HttpResponseRedirect
# Create your views here.
def home(request):
    return render(request, 'index.html')


def register(request):
    if (request.method=='POST'):
        name= request.POST['n']
        age=request.POST['a']
        email=request.POST['e']
        address=request.POST['ad']
        password= request.POST['p']
        files= request.FILES['f']
        fs=FileSystemStorage() #fs is a object here ,filesystemstorage is a class 
        fs.save('static/userpics/'+ files.name,files)
        sql='insert into user_tb(name,age,address,email,password,photo)values("'+name+'","'+age+'","'+address+'","'+email+'","'+password+'","'+files.name+'")'
        dbconnection.insert_data(sql)
        return HttpResponseRedirect('register?suc=1')# register is the url 
    if (request.GET.get('suc')):
        msg='registered successfully'
        return render (request,'register.html',{'m':msg})
    return render (request,'register.html')
        


def login(request):
    if(request.method=='POST'):
        email=request.POST['e']
        password= request.POST['p']
        sql='select * from user_tb where email="'+email+'" and password="'+password+'"'
        data=dbconnection.selectonerecord(sql)
        if (data):
            request.session['log_id']=email
            return HttpResponseRedirect('userhome')
    return render (request,'login.html')
    
    
    
def userhome(request):
    z=request.session['log_id']
    sql='select * from user_tb where email ="'+z+ '"'
    data=dbconnection.selectonerecord(sql)
    
    
    return render(request,'userhome.html',{'user_data': data})

def edit(request):
    z=request.GET.get('em')
    if (request.method=='POST'):
        name= request.POST['n']
        age=request.POST['a']
        email=request.POST['e']
        address=request.POST['ad']
        password= request.POST['p']
        sql = 'update user_tb set name = "'+name+'",age= "'+age+'",address="'+address+'",email = "'+email+'",password="'+password+'" where email = "'+z+'"'
        dbconnection.update_data(sql)
        return HttpResponseRedirect('userhome')
    sql='select * from user_tb where email ="'+z+ '"'
    data=dbconnection.selectonerecord(sql)
    return render(request,'edit.html',{'user_data': data})

def logout(request):
    request.session.clear()
    return HttpResponseRedirect('login')

def mygallery(request):
    em = request.session['log_id']
    if(request.method=='POST'):
        title=request.POST['title']
        filetype=request.POST['filetype']
        file=request.FILES['file']
        f=FileSystemStorage()
        f.save('static/uploadpics/'+file.name,file)
        sql='insert into upload_data(title, filetype,file,email) values ("'+title+'","'+filetype+'","'+file.name+'","'+em+'")'
        dbconnection.insert_data(sql) 
        return HttpResponseRedirect('mygallery') #goes to apps urls mygallery
        
        
        
    return render(request,'mygallery.html')

def image(request):
    em=request.session['log_id']
    sql = 'select * from upload_data where email = "'+em+'" and filetype = "1"'
    database=dbconnection.selectrecord(sql)
    
    return render(request,'image.html', {'d':database})


def audio(request):
    em=request.session['log_id']
    sql = 'select * from upload_data where email = "'+em+'" and filetype = "2"'
    database=dbconnection.selectrecord(sql)
    
    return render(request,'audio.html', {'d':database})

def video(request):
    em=request.session['log_id']
    sql = 'select * from upload_data where email = "'+em+'" and filetype = "3"'
    database=dbconnection.selectrecord(sql)
    
    return render(request,'video.html',{'d':database})




