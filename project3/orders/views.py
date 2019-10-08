from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.shortcuts import render
from django.urls import reverse
from .models import Menu, Cart, UserProfile

# Create your views here.
# If not logged in, redirected to login.
def index(request):
    if not request.user.is_authenticated:
        return render(request, "orders/login.html", {"message": None})
    context = {
        "user": request.user
    }
    return render(request, "orders/index.html", context)


# Login page
def login_view(request):
    username = request.POST["username"]
    password = request.POST["password"]
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "orders/login.html", {"message": "Invalid credentials."})

# Logs user out
def logout_view(request):
    logout(request)
    return render(request, "orders/login.html", {"message": "Logged out."})


# To register. Asks user for 6 text fields but only really uses 3
def register(request):
    if request.method == "POST":
        # collects info
        fname = request.POST["fname"]
        lname = request.POST["lname"]
        username = request.POST["username"]
        password = request.POST["password"]
        confirm = request.POST["confirm"]
        email = request.POST["email"]

        # Checks to see that passwords match
        if password != confirm:
            return render(request, "orders/register.html",
                        {"message": "Username already taken."})
        # if username exists, error
        if User.objects.filter(username=username).exists():
            return render(request, "orders/register.html", {"message": "Username already exists."})

        # creates user, cart, and userProfile
        user = User.objects.create_user(username=username, password=password)
        user.save()
        cart = Cart.objects.create(items=[])
        cart.save()
        userProfile = UserProfile.objects.create(user=user, username=username, cart=cart)
        userProfile.save()
        return render(request, "orders/login.html")
    else:
        return render(request, "orders/register.html")


# An about page
def about(request):
    return render(request, "orders/about.html")


# shopping cart
def cart(request):
    # gets the cart of the current user
    user = UserProfile.objects.get(username=request.user.username)
    cart = user.get_cart()


    if request.method == "POST":
        # if user places order, clears cart and sends message
        cart.removeAll()
        cart.save()
        context = {
            "message": 'Your order has been placed'
        }
        return render(request, "orders/cart.html", context)
    else:
        # to display cart items
        prices = []
        non_custom = 0

        # appends prices of all items to list
        for i in range(len(cart.items)):
            order = Menu.objects.get(category=cart.items[i][6:])
            # if not custom, just add regular price
            if not order.custom:
                # separates small and large items
                if cart.items[i].startswith('S'):
                    prices.append(order.smallPrice)
                else:
                    prices.append(order.largePrice)
                non_custom += 1
            else:
                # if custom item, multiply number of toppings by specified topping price
                toppingPrice = order.toppingPrice
                totalAddedPrice = toppingPrice * len(cart.addOns[cart.items[i]])
                # makes sure toppings array actually has toppings in it
                if cart.addOns[cart.items[i]][0] == "":
                    if cart.items[i].startswith('S'):
                        prices.append(order.smallPrice)
                    else:
                        prices.append(order.largePrice)
                else:
                    # seprates small and large items
                    if cart.items[i].startswith('S'):
                        prices.append(order.smallPrice + totalAddedPrice)
                    else:
                        prices.append(order.largePrice + totalAddedPrice)
        context = {
            "cart": cart.items,
            "prices": prices
        }
        return render(request, "orders/cart.html", context)


# page where custom toppings are listed
def addons(request):
    return render(request, "orders/addons.html")


# menu. User can add things to his/her cart from here, and select toppings
def menu(request):
    # gets current user's cart
    user = UserProfile.objects.get(username=request.user.username)
    cart = user.get_cart()

    if request.method == "POST":
        # collects added items from page
        added_items = request.POST.getlist('cb[]')
        addOns = request.POST.getlist('addOns[]')
        prices = []

        # if user has selected anything
        if added_items:
            non_custom = 0

            # iterates through selections
            for i in range(len(added_items)):
                # adds items to the cart database
                cart.add_item(added_items[i])
                cart.addOn(addOns[i], added_items[i])
                order = Menu.objects.get(category=added_items[i][6:])
                # Differentiates between custom and non-custom order prices and appends price to list 
                if not order.custom:
                    if added_items[i].startswith('S'):
                        prices.append(order.smallPrice)
                    else:
                        prices.append(order.largePrice)
                    non_custom += 1
                else:
                    toppingPrice = order.toppingPrice
                    totalAddedPrice = toppingPrice * len(addOns[i - non_custom].split(','))
                    if addOns[i - non_custom].split(',')[0] == "":
                        if added_items[i].startswith('S'):
                            prices.append(order.smallPrice)
                        else:
                            prices.append(order.largePrice)
                    else:
                        if added_items[i].startswith('S'):
                            prices.append(order.smallPrice + totalAddedPrice)
                        else:
                            prices.append(order.largePrice + totalAddedPrice)
        cart.save()
        context = {
            "cart": cart.items,
            "prices": prices
        }
        return render(request, "orders/cart.html", context)
    else:
        context = {
            "menu": Menu.objects.all()
        }
        return render(request, "orders/menu.html", context)
