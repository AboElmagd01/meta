from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from .form import Dateform
from .models import Room, Dish, Offer, Reservation
from django.contrib.auth import login, authenticate, logout
# from django.contrib.auth.models import User
from django.shortcuts import render, redirect
import datetime


# Create your views here.

def mainApp(request):
    return render(request, "Teplates/index.html")


def about(request):
    return render(request, "Teplates/about.html")


def contact(request):
    return render(request, "Teplates/contact.html")


def explore(request):
    return render(request, "Teplates/explore.html")


def map(request):
    return render(request, "Teplates/map.html", {'location': "Cairo"})


def mapAlex(request):
    return render(request, "Teplates/map.html", {'location': "Alex"})


def mapGiza(request):
    return render(request, "Teplates/map.html", {'location': "Giza"})


def mapSharm(request):
    return render(request, "Teplates/map.html", {'location': "Sharm"})


def mapLuxor(request):
    return render(request, "Teplates/map.html", {'location': "Luxor"})


def spa(request):
    return render(request, "Teplates/spa.html")


# Admin Panel
def resta(request):
    return render(request, "Teplates/restaurant.html", {'meals': Dish.objects.all()})


def rooms(request):
    dates = []
    for i in range(7):
        date = datetime.datetime.now() + datetime.timedelta(days=i)
        date_str = date.strftime("%A, %d/%m")
        dates.append(date_str)
        rooms_not = Room.objects.filter(reservation__spot=date)
        if rooms_not.count() > 0:
            for room in rooms_not:
                x = list(room.notavailable)
                v = Reservation.objects.get(room=room, spot=date)
                days = int(v.to.strftime("%d")) - int(datetime.date.today().strftime("%d")) + 1
                j = i
                while j < days and j < 7:
                    x[j] = 'F'
                    print(x)
                    j += 1
                room.notavailable = ''.join([str(elem) for elem in x])
                room.save()
    return render(request, "Teplates/rooms.html", {'rooms': Room.objects.all(), 'dates': dates})


def offers(request):
    return render(request, "Teplates/offers.html", {'offers': Offer.objects.all()})


# # User
def feed(request):
    return render(request, "Teplates/feedBack.html")


def login_v(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            return render(request, "Teplates/login.html", {'text': 0})
    else:
        return render(request, "Teplates/login.html")


def register(request):
    if request.method == 'POST':
        username = request.POST.get("user_name")
        user_email = request.POST.get("user_email")
        password = request.POST.get("user_password")
        user1 = User.objects.all().filter(username=username)
        if user1.count() > 0:
            return render(request, "Teplates/registration.html", {'text': 0})
        else:
            user = User.objects.create_user(username=username, email=user_email, password=password)
            if user is not None:
                login(request, user)
            return redirect('/')
    else:
        return render(request, "Teplates/registration.html", {'text': 1})


def logout_view(request):
    logout(request)
    return redirect('/')


def room_view(request, id):
    if not request.user.is_authenticated:
        return redirect('/login')
    room = Room.objects.get(id=id)
    if request.method == "POST":
        form = Dateform(request.POST)
        room = Room.objects.get(id=id)
        username = request.user
        if form.is_valid():
            fdate = form.cleaned_data['fromdate']
            tdate = form.cleaned_data['todate']
            filter_params = dict(spot=fdate,
                                 to=tdate)
            # checking if Exists
            rese = Reservation.objects.filter(**filter_params, room=room).exists()
            # Validate date
            valid_date = fdate > tdate
            if rese or valid_date:
                return render(request, "Teplates/room.html", {'room': room, 'form': form, 'text': 0})
            # Checking Intervals
            reseQ = Reservation.objects.filter(room=room)
            dont = False
            for re in reseQ:
                if re.spot <= fdate and re.to >= tdate:
                    dont = True
                elif re.spot >= fdate and re.to <= tdate:
                    dont = True
                elif re.spot <= fdate <= re.to:
                    dont = True
                elif re.spot <= tdate <= re.to:
                    dont = True
            if rese or dont:
                return render(request, "Teplates/room.html", {'room': room, 'form': form, 'text': 0})
            Reservation.objects.create(user=username, room=room, spot=fdate, to=tdate)
        return redirect("/reserve")

    else:
        form = Dateform()
        return render(request, "Teplates/room.html", {'room': room, 'form': form, 'text': 1})


def reservation_view(request):
    if not request.user.is_authenticated:
        return redirect('/login')
    reserve = Reservation.objects.filter(user=request.user)
    return render(request, "Teplates/reserve.html", {'reserves': reserve})


def deleteview(request, id):
    if not request.user.is_authenticated:
        return redirect('/login')
    r = Room.objects.get(reservation__id=id)
    v = Reservation.objects.get(id=id)
    day = int(v.spot.strftime("%w")) - int(datetime.date.today().strftime("%w"))
    days = int(v.to.strftime("%d")) - int(datetime.date.today().strftime("%d")) + 1
    x = list(r.notavailable)
    j = day
    while j < days and j < 7:
        x[j] = 'T'
        j += 1
    r.notavailable = ''.join([str(elem) for elem in x])
    r.save()
    v.delete()
    return redirect('/reserve')
