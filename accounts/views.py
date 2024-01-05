from django.shortcuts import render,get_object_or_404,redirect
from django.contrib import messages
from accounts.models import Contact,Place
from datetime import datetime
from django.contrib.auth.models import User #for Registration
from django.contrib.auth import authenticate,login,logout

from django.contrib.auth import get_user_model
User = get_user_model()

# Create your views here.

def demo(request):
    return render(request,'demo.html')

def index(request):
    print(request.user.id)
    print(request.user.is_anonymous)
    myPlaces = Place.objects.all().values()
    
    return render(request,"index.html",{'myPlaces': myPlaces})

def about(request):
    return render(request,'about.html')

def services(request):
    return render(request,'services.html')

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        contact = Contact(name=name,email=email,phone=phone,message=message,date=datetime.today())
        contact.save()
        messages.success(request, "You message has been sent!!")

    return render(request,'contact.html')

def registerUser(request):
    if not request.user.is_anonymous:
        return redirect('/')
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirmPassword = request.POST.get('confirmPassword')
        if password == confirmPassword:
            user = User.objects.create_user(email, password)
            user.save()
            login(request, user)
            return redirect(index)
        
    return render(request,'register.html')

def loginUser(request):
    if not request.user.is_anonymous:
        return redirect('/')
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        print(request.POST.get('password'))
        user = authenticate(request,email=email, password=password)
        print(user)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            messages.error(request, "Invalid Credintial!!")
    return render(request,'login.html')

def logoutUser(request):
    logout(request)
    return redirect('/')

def dashboard(request):
    if  request.user.is_anonymous:
        return redirect('/')
    
    myPlaces = Place.objects.filter(user=request.user).values()
    print(myPlaces)
    if request.method == "POST":
        firstName = request.POST.get("firstName")
        lastName = request.POST.get("lastName")
        phone_number = request.POST.get("phone")
        address = request.POST.get("address")
        request.user.first_name = firstName
        request.user.last_name = lastName
        request.user.phone_number = phone_number
        request.user.address = address
        request.user.save()
        messages.success(request, "Profile Updated!!!")

    return render(request,'dashboard.html',{'myPlaces': myPlaces})


def addPlace(request):
    if request.user.is_anonymous:
        return redirect('/')
    # if request.method == "POST":
    if request.method == 'POST' and request.FILES['image']:
        place_name = request.POST.get('placeName')
        place_type = request.POST.get('placeType')
        address = request.POST.get('address')
        description = request.POST.get('description')
        image = request.FILES['image']
        place = Place(place_type=place_type,
                      name=place_name,
                      description=description,
                      address=address,
                      images=image,
                      user=request.user)
        place.save()
        messages.success(request, "You message has been sent!!")

    return render(request,'addPlace.html')

def edit(request,id):
    if request.user.is_anonymous:
        return redirect('/')
    
    myPlaces = Place.objects.get(place_id=id)
    print(myPlaces)
    if request.method == 'POST':
        place_name = request.POST.get('placeName')
        place_type = request.POST.get('placeType')
        address = request.POST.get('address')
        description = request.POST.get('description')
        new_image = request.FILES.get('image')
        myPlaces.place_type=place_type
        myPlaces.name=place_name
        myPlaces.description=description
        myPlaces.address=address
        print(new_image)
        print(myPlaces.images)
        if new_image != None or new_image != myPlaces.images:
            myPlaces.images=new_image
        myPlaces.save()
        # myPlaces.update(place_type=place_type,name=place_name,description=description,address=address,images=image,)
        messages.success(request, "Place Edited !!!")

    return render(request,'edit.html',{'myPlace': myPlaces})


def viewPlace(request,id):
    myPlace = Place.objects.get(place_id=id)
    print(myPlace.place_id)
    print(request.user)
    if request.method == 'POST':
        review = request.POST.get('review')
        rating = request.POST.get('rating')
        images = request.FILES.getlist('images')
        print(review)
        print(rating)
        for image in images:
            print(image)
        messages.success(request, "submitted")
    return render(request,'viewPlace.html',{'myPlace':myPlace})