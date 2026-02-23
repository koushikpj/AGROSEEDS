from django.contrib import admin
from django.urls import path
from .views import etrade, index, crop_pred, predict,sign_in,sign_up,sign_out,feedback,FeedbackAction,cartaction,viewcart

urlpatterns = [
    #path('',index,name='homepage'),
    path('', sign_in, name='login'),
    path('index',index,name='homepage'),
    path('etrade',etrade, name='etradpage'),
    path('feedback',feedback, name='feedbackpage'),
    path('cartaction',cartaction, name='cartaction'),
    path('FeedbackAction',FeedbackAction, name='FeedbackAction'),
    path('viewcart',viewcart, name='cartpage'),



    path('crop_prediction',crop_pred,name='croppredpage'),
    path('predict',predict, name='predict'),
    path('register/', sign_up, name='register'),
    path('logout/', sign_out, name='logout'),

]
