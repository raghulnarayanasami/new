from django.shortcuts import render
from myapp.myapp.functions.functions import handle_uploaded_file
from myapp.forms import StudentForm
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate,login, logout
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
import boto3
# Create your views here.

user2=''
def user_login(request):
    global user2
    global user1
    context = {}
    if request.method =="POST":
        username = request.POST['username']
        password=request.POST['password']
        user1=authenticate(request,username=username,password=password)
        if user1:
           login(request, user1)
           return HttpResponseRedirect(reverse('storage'))
        else:
            context['error']="Please provide valid credentials!!!"
            return render(request, 'myapp/index.html', context)

    else:
        return render(request, 'myapp/index.html', context)
            
       
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

def storagedata(request):
    return  render(request, 'myapp/data.html', context=None)

@csrf_exempt
def s3bucket(request):
  
    if request.method == 'POST':
        context = {}
        student = StudentForm(request.POST, request.FILES)
        bucketname = request.POST['bucketname']
        file_obj = request.FILES['file']
        filename = str(file_obj.name)
        if student.is_valid():
            bucket_list = bucketlist()
            for bucket in bucket_list:
                if bucket.name == str(bucketname):
                   context['error']="The Bucket Name already exists.Choose other Buket Name"
                   return render(request, 'myapp/message.html', context)

            handle_uploaded_file(request.FILES['file'])
            uploadfile = "/root/demoproject/myapp/static/upload/"+filename
            boto3connection(bucketname, filename, uploadfile)
            context['error']="The NEW CONTRAINER is created : " + bucketname + " and The FIle is Uploaded Successfully in that Bucket"
            return render(request, 'myapp/message.html', context)
    else:
        student = StudentForm()
        return render(request, "myapp/s3.html", {'form': student})

def boto3connection(bucketname, filename, uploadfile):

    host='https://aos.tcsecp.com'
    access_key = '47cd575d659d468aa5aa3f7a4cfa8a89'
    secret_key = 'a87b5287abb7484683e81f78c1c2cbf9'

    s3=boto3.resource('s3',aws_access_key_id=access_key,aws_secret_access_key=secret_key, endpoint_url=host,)

    s3.create_bucket(Bucket=bucketname)
    s3.Object(bucketname,filename).upload_file(Filename=uploadfile)

def bucketlist():
    host='https://aos.tcsecp.com'
    access_key = '47cd575d659d468aa5aa3f7a4cfa8a89'
    secret_key = 'a87b5287abb7484683e81f78c1c2cbf9'

    s3=boto3.resource('s3',aws_access_key_id=access_key,aws_secret_access_key=secret_key, endpoint_url=host,)
    bucket_list = s3.buckets.all()
    return bucket_list

