from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models.product import Product
from .models.category import Category
from .models.feedback import Feedback
from .models.cart import cart
import datetime

from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.urls import reverse
import joblib
from .forms import LoginForm, RegisterForm
# Create your views here.

def sign_up(request):
    if request.method == 'GET':
        form = RegisterForm()
        return render(request, 'register.html', {'form': form})    
   
    if request.method == 'POST':
        form = RegisterForm(request.POST) 
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            messages.success(request, 'You have singed up successfully.')
            login(request, user)
            return redirect('etradpage')
        else:
            return render(request, 'register.html', {'form': form})

def sign_in(request):

    if request.method == 'GET':
        form = LoginForm()
        return render(request,'login.html', {'form': form})
    
    elif request.method == 'POST':
        form = LoginForm(request.POST)
        
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request,username=username,password=password)
            if user:
                login(request, user)
                messages.success(request,f'Hi {username.title()}, welcome back!')
                return redirect('etradpage')
        
        # form is not valid or user is not authenticated
        messages.error(request,f'Invalid username or password')
        return render(request,'login.html',{'form': form})

def etrade(request):
    products = Product.get_all_products()
    categories = Category.get_all_categories()
    category_id = request.GET.get('category')
    if category_id:
        products = Product.get_all_products_by_category_id(category_id)
    else:
        products = Product.get_all_products()
    data = {}
    data['products'] = products
    data['categories'] = categories
    current_user=request.user
    data['username']=current_user
    return render(request,'etrade.html',data)


def feedback(request):
    data = {}
    current_user=request.user
    data['username']=current_user
    return render(request,'feedback.html',data)
def viewcart(request):
    data = {}
    current_user=request.user
    data['username']=current_user
    return render(request,'viewcart.html',data)



def index(request):
    return render(request,'index.html')

def crop_pred(request):
    return render(request,'crop_pred.html')

def FeedbackAction(request):
    if request.method == 'POST':
   
        username = request.POST.get('t0', False)
        fback = request.POST.get('t1', False)
        feedback=Feedback.objects.create(uname=username,feedback=fback)
        #feedback.save(force_insert=True )
    return HttpResponseRedirect(reverse('homepage'))
def predict(request):
    data = []
    data.append(request.POST.get('tempVal'))
    data.append(request.POST.get('humidityVal'))
    data.append(request.POST.get('phVal'))
    data.append(request.POST.get('rainfallVal'))

    md = joblib.load('final_model.sav')
    predictcrop=[data]
    # Putting the names of crop in a single list
    crops=['wheat','mungbean','Tea','millet','maize','lentil','jute','cofee','cotton','ground nut','peas','rubber','sugarcane','tobacco','kidney beans','moth beans','coconut','blackgram','adzuki beans','pigeon peas','chick peas','banana','grapes','apple','mango','muskmelon','orange','papaya','watermelon','pomegranate']
    cr='rice'
    predictions = md.predict(predictcrop)
    count=0
    for i in range(0,30):
        if(predictions[0][i]==1):
            c=crops[i]
            count=count+1
            break
        i=i+1
    if(count==0):
        context = {'ans': cr}
    else:
        context = {'ans': c}
    return render(request,'crop_pred.html',context)

def sign_out(request):
    logout(request)
    messages.success(request,f'You have been logged out.')
    return redirect('login')        

def cartaction(request):
    if request.method == 'POST':
   
        username = request.POST.get('t1', False)
        pname = request.POST.get('t2', False)
        cd=datetime.datetime.now()
        print("data",username,pname,cd)
        ct=cart.objects.create(uname=username,product=pname,cdate=cd)
        #feedback.save(force_insert=True )
    return HttpResponseRedirect(reverse('cartpage'))