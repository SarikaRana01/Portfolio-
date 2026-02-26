from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib.auth import authenticate,login as login_acc,logout as logout_acc
from accounts.models import Address,Phone
from django.contrib import messages
# Create your views here.

def show(request):
 if request.user.is_authenticated:
    user=User.objects.get(username=request.user)
    addr=Address.objects.filter(user=user)
    phn=Phone.objects.filter(user=user)
    context={"users":user,"addr":addr,"phn":phn}
    return render(request,"accounts/show.html",context)
 return render(request,"accounts/login.html")

def register(request):
    if request.method=="POST":
        username=request.POST.get("username")
        fName=request.POST.get("fName")
        lName=request.POST.get("lName")
        email=request.POST.get("email")
        passwd=request.POST.get("passwd")
        if(username in User.objects.values_list("username",flat=True)):
            return HttpResponse("Username already Exists...")
        user=User.objects.create_user(username=username,email=email,first_name=fName,last_name=lName)
        user.set_password(passwd)
        user.save()
        context={"user":user}
        messages.success(request,"Account created successfully")
        return render(request,"accounts/login.html")
    messages.warning(request,"Account not exists")
    return render(request,"accounts/register.html")



def login(request):
    if request.method=="POST":
        username=request.POST.get("username")
        passwd=request.POST.get("passwd")
        user=authenticate(request,username=username,password=passwd)
        if user is not None:
            login_acc(request,user)
            messages.success(request,"Logged in successfully")
            return redirect("show")
    messages.warning(request,"Invalid username or password!")
    return render(request,"accounts/login.html")

def logout(request):
    logout_acc(request)
    return redirect("login")
    

def address(request):
     user=User.objects.get(username=request.user)
     context={"user":user}
     username=request.POST.get("username")
     if request.method=="POST" and user.username==username :
        username=request.POST.get("username")
        state=request.POST.get("state")
        distt=request.POST.get("distt")
        city=request.POST.get("city")
        pin=request.POST.get("pin")
        add=Address.objects.create(user=request.user,state=state,distt=distt,city=city,pincode=pin)
        add.save()
        messages.success(request,"Address added successfully")
        return redirect("show")
     return render(request,"accounts/address.html",context)
        
    
def phone(request):
     user=User.objects.get(username=request.user)
     context={"user":user}
     username=request.POST.get("username")
     if request.method=="POST" and user.username==username :
        username=request.POST.get("username")
        phone=request.POST.get("phone")
        count=0
        temp=""
        for i in range(len(phone)):
            if count==0 and phone[i]==0:
                temp+="+91"
            else:
                temp+=phone[i]
        if temp[0]!='+':
            temp="+91" + temp 
        if(len(temp)==13):
            phn=Phone.objects.create(user=request.user,phone=temp)
            phn.save()
            messages.success(request,"Phone no. added successfully")
            return redirect("show")
        elif(len(temp)>13):
            messages.warning(request,"Phone no. can't be more than 10 digits")
            return render(request,"accounts/phone.html",context)
        else:
            messages.warning(request,"Phone no. can't be less than 10 digits")
            return render(request,"accounts/phone.html",context)
     return render(request,"accounts/phone.html",context)


def edit_no(request,id):
     phn=Phone.objects.get(id=id)
     username=request.POST.get("username")
     context={"phn":phn}
     if request.method=="POST" and phn.user.username==username :  
        phone=request.POST.get("phone")
        count=0
        temp=""
        for i in range(len(phone)):
            if count==0 and phone[i]==0:
                temp+="+91"
            else:
                temp+=phone[i]
        if temp[0]!='+':
            temp="+91" + temp 
        if(len(temp)==13):
            phn.phone=temp
            phn.save()
            messages.success(request,"Phone no. updated successfully")
            return redirect("show")
        elif(len(temp)>13):
            messages.warning(request,"Phone no. can't be more than 10 digits")
            return render(request,"accounts/phone_edit.html",context)
        else:
            messages.warning(request,"Phone no. can't be less than 10 digits")
            return render(request,"accounts/phone_edit.html",context)
     return render(request,"accounts/phone_edit.html",context)
     

def edit_addr(request,id):
     username=request.POST.get("username")
     addr=Address.objects.get(id=id)
     context={"addr":addr}
     if request.method=="POST" and addr.user.username==username :
        username=request.POST.get("username")
        state=request.POST.get("state")
        distt=request.POST.get("distt")
        city=request.POST.get("city")
        pin=request.POST.get("pin")
        addr.state=state
        addr.distt=distt
        addr.city=city
        addr.pincode=pin
        addr.save()
        messages.success(request,"Address updated successfully")
        return redirect("show")
     return render(request,"accounts/address_edit.html",context)


def delete_addr(request,id):
     addr=Address.objects.get(id=id)
     if addr.user==request.user:
         addr.delete()
         return redirect("show")
     messages.warning(request,"Unauthorized access")
     return redirect("show")

def delete_no(request,id):
     phn=Phone.objects.get(id=id)
     if phn.user==request.user:
         phn.delete()
         return redirect("show")
     messages.warning(request,"Unauthorized access")
     return redirect("show")