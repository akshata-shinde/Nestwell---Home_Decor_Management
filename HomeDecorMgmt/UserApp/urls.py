from django.urls import path
from . import views 

urlpatterns = [
    path('', views.home),
    path('ShowProducts/<id>',views.ShowProducts),
    path('ViewDetails/<id>',views.ViewDetails),
    path('Login',views.Login),
    path('SignUp',views.SignUp),
    path('SignOut',views.SignOut),
    path('addToCart',views.addToCart),
    path('showCartItems',views.showCartItems),
    path('MakePayment',views.MakePayment),
    path('aboutus',views.aboutus),
    path('deals',views.deals),
    path('contactus',views.contactus),
]