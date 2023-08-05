from django.shortcuts import render,redirect
from AdminApp.models import Category,Product,Payment
from UserApp.models import UserInfo,MyCart,OrderMaster
#from django.http import HttpResponse
from django.contrib import messages

# Create your views here.
def home(request):
    cats = Category.objects.all()
    products = Product.objects.all()
    return render(request,"master.html",{"cats":cats,"products":products})

def ShowProducts(request,id):
    cats = Category.objects.all()
    products = Product.objects.filter(category = id)
    return render(request,"master.html",{"cats":cats, "products": products})

def ViewDetails(request,id):
    cats = Category.objects.all()
    product = Product.objects.get(id=id)
    return render(request,"ViewDetails.html",{"cats":cats, "product": product})

def addToCart(request):
    if("uname" in request.session):
        #get your info
        user = UserInfo.objects.get(username = request.session["uname"])
        #getting prod info
        product_id = request.POST["pid"]
        product = Product.objects.get(id=product_id)
        qty = request.POST["qty"]
        try:
            item = MyCart.objects.get(user=user,product=product)
        except:
            cart = MyCart()
            cart.user = user
            cart.product = product
            cart.qty = qty
            cart.save()
            messages.info(request,"Product Successfully Added in Cart")
            #return redirect(showCartItems)
        else:
            #return HttpResponse("Already in Cart")
            messages.info(request,"Product Already in Cart")
        return redirect(showCartItems)
    else:
        return redirect(Login)

def showCartItems(request):
    cats = Category.objects.all()
    if(request.method == "GET"):
        items = MyCart.objects.filter(user = request.session["uname"])
        total = 0
        for item in items:
            total += item.qty*item.product.price
        request.session["total"] = total
        return render(request,"showAllCartItems.html",{"items":items,"cats":cats})
    else:
        product_id = request.POST["product_id"]
        item = MyCart.objects.get(id=product_id)
        action = request.POST["action"]
        if(action == "remove"):
            item.delete()
        else:
            qty = request.POST["qty"]
            item.qty = qty
            item.save()
        return redirect(showCartItems)

def contactus(request):
    cats = Category.objects.all()
    return render(request,"contactus.html",{'cats':cats})


def deals(request):
    cats = Category.objects.all()
    return render(request,"deals.html",{'cats':cats})


def MakePayment(request):
    if(request.method == "GET"):
        return render(request,"MakePayment.html",{})
    else:
        card_no = request.POST["card_no"]
        cvv = request.POST["cvv"]
        expiry = request.POST["expiry"]
        try:
            buyer = Payment.objects.get(card_no=card_no,cvv=cvv,expiry=expiry)
        except:
            return redirect(MakePayment)
        else:
            owner = Payment.objects.get(card_no='222',cvv='222',expiry='11/2025')
            buyer.balance -= float(request.session["total"])
            owner.balance += float(request.session["total"])
            buyer.save()
            owner.save()

            myorder = OrderMaster()
            user = UserInfo.objects.get(username=request.session["uname"])
            myorder.user  = user
            myorder.amount = request.session["total"]
            items = MyCart.objects.filter(user=user)
            details = ""
            for item in items:
                details+= item.product.product_name+" "
                item.delete()

            myorder.details= details
            myorder.save()

            #delete all cart items

            return redirect(home)
        
def SignOut(request):
    #delete the session
    request.session.clear()
    return redirect(home)

def Login(request):
    
    if(request.method=="GET"):
        return render(request,"Login.html",{})
    else:
        uname = request.POST["uname"]
        pwd = request.POST["pwd"]
        try:
            #If user is already present
            user = UserInfo.objects.get(username=uname,password=pwd)            
        except:
            #Login fail
           message = "Invalid Credentials, Please Try Again!!"
           return render(request,"Login.html",{"message":message})
           #messages.info(request,"Login Successfully!!")
        else:
            #if login successful then create a session for that user
            request.session["uname"]=uname
            return redirect(home)

def SignUp(request):
    if(request.method=="GET"):
        return render(request,"SignUp.html",{})
    else:
        uname = request.POST["uname"]
        pwd = request.POST["pwd"]
        try:
            #If user is already present
            user = UserInfo.objects.get(username=uname)            
        except:
            #We can create user, if user is not present
            user = UserInfo(uname,pwd)
            user.save()
            return redirect(home)
         
        else:
            message = "User Already Exist"
            return render(request,"SignUp.html",{"message":message})
            
def aboutus(request):
    cats = Category.objects.all()
    return render(request,"aboutus.html",{'cats':cats})