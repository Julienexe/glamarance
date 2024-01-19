from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login as auth_login,authenticate, logout
from django.http import HttpResponseRedirect, Http404, HttpResponse
from django.shortcuts import reverse
from order.views import make_order

#logins
def login(request):
    if request.method == "POST": 
        email = request.POST.get("email")
        password = request.POST.get("password")
        user = authenticate(request, username=email, password=password)
        if user is not None:
            auth_login(request, user)
            return make_order(request)
        else:
            return redirect("order:order_create")
    return redirect("shop:product_list")
    

#logout
@login_required
def logout_view(request):
    logout(request)
    return redirect("shop:shop_index")

@login_required
def place_order(request):
    return make_order(request)

