from os import stat
from django.shortcuts import render,redirect
from .models import Hiretuber
from django.contrib import messages

# Create your views here.
def hiretuber(request):
    if request.method=="POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        tuber_id = request.POST['tuber_id']
        tuber_name = request.POST['tuber_name']
        user_id = request.POST['user_id']
        email = request.POST['email']
        phone = request.POST['phone']
        city = request.POST['city']
        state = request.POST['state']
        message = request.POST['message']

        hiretuber = Hiretuber(first_name=first_name, last_name=last_name, tuber_name=tuber_name,tuber_id=tuber_id,
        user_id=user_id,email=email, phone= phone, city=city, state=state, message=message)
        hiretuber.save()
        messages.success(request,"Thanks for contacting us. We will get back soon")
        return redirect('youtubers')