from django.urls import path, include
from rest_framework import urls
#from . import views
from rest_auth.registration.views import RegisterView
from .serializers import CustomRegisterSerializer
from .views import AccountActivateView

urlpatterns =[
    path('api-auth/', include('rest_framework.urls')),
    
    #path('signup/', views.UserCreate.as_view()),
    path('rest-auth/',include('rest_auth.urls')),
    #path('rest-auth/registration/', include('rest_auth.registration.urls')),
    path('', include('allauth.urls')),
    path('rest-auth/registration/', RegisterView.as_view(serializer_class=CustomRegisterSerializer), name='rest_register'),
    path('activate/<str:uidb64>/<str:token>/', AccountActivateView.as_view(), name='account-activate'),
 ]