from django.contrib import auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.urls import reverse
import requests
import json
import time

from .models import Profile

regex = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'

cn = 160220004993
bun = 4597
ct = 1

class MahaDiscomf(object):
    """ Class to get details about Mahadiscom """

    def __init__(self, cn, bun, ct):
        """ __init__ """
        self.serverurl = 'https://wss.mahadiscom.in/wss/'
        self.con_details = {}
        self.con_details['ConsumerNo'] = cn
        self.con_details['BuNumber'] = bun
        self.con_details['consumerType'] = ct

    def is_consumer_valid(self):
        """
        Helper function to check if consumer is valid or not
        returns : True if consumer is valid
                  False if consumer is not valid
        """
        actionurl = 'wss?uiActionName=validateConsumerNumberHTLT&IsAjax=true'
        url = self.serverurl + actionurl
        response = requests.post(url, data=self.con_details)
        if response.status_code != 200:
            return False
        elif response.text == 'false':
            return False
        elif response.text == 'true':
            return True

    def get_bill_details(self):
        """
        Function to get bill details
        returns : a dictionary with consumer's bill details
        """
        billdetails = {}
        actionurl = "wss?uiActionName=postViewPayBill&IsAjax=true"
        url = self.serverurl + actionurl
        response = requests.post(url, data=self.con_details)
        try:
            billdetails = json.loads(response.text)
        except ValueError as err:
            print("Unable to parse json response" + str(err))

        if response.status_code == 200:
            return billdetails
        else:
            print("ERROR: Return code is Non-2xx : %d" % response.status_code)
            return {}


def createpost(request):
    if request.method == 'POST':
        return redirect(reverse('forms'))
    else:
        return render(request, 'app/signup.html')


def forms(request):
    email = request.POST.get('email')
    password = request.POST.get('password')
    user = User.objects.create_user(username=email, password=password)
    profile = Profile(user=user)
    auth.login(request, user)
    profile.save()
    if request.method == "POST":
        return render(request, "app/forms.html")
    else:
        return render(request, "app/forms.html")


def mahadiscomf(request):
    profile = Profile.objects.get(user=request.user)
    if request.method == 'GET':

        #mahadiscom = MahaDiscomf(cn='160220004993', bun='4597', ct='1')
        #billdetails = mahadiscom.get_bill_details()
        #profile.electricity = billdetails['consumptionUnits']
        #profile.save()

        mahadiscom = MahaDiscomf(cn=cn, bun=bun, ct=ct)
        billdetails = mahadiscom.get_bill_details()
        profile.electricity = billdetails['consumptionUnits']
        print(billdetails['consumptionUnits'])
        profile.save()
        return render(request, 'app/mahadiscom.html')

    else:
        return render(request, 'app/mahadiscom.html')


def myview(request):

    if request.method == "POST":
        profile = Profile.objects.get(user=request.user)
        profile.name = request.POST.get('name')
        profile.age = request.POST.get('age')
        profile.country = request.POST.get('country')
        profile.diet = request.POST.get('optradio')
        profile.car_fuel = request.POST.get('optradio1')
        profile.scooter = request.POST.get('optradio2')
        profile.family = request.POST.get('family')
        profile.electricity = request.POST.get('optradio3')
        profile.diet = int(profile.diet)
        profile.car_fuel = int(profile.car_fuel)
        profile.scooter = int(profile.scooter)
        profile.family = int(profile.family)
        profile.electricity = int(profile.electricity)
        profile.save()
        return render(request, 'app/imagemap_house.html')
    else:
        return render(request, 'app/imagemap_house.html')


def myoutview(request):
    return render(request, 'app/imagemap_outdoor.html')


def food(request):
    profile = Profile.objects.get(user=request.user)
    profile.meal += 1
    profile.save()
    return render(request, 'app/food.html')


def shopping(request):
    profile = Profile.objects.get(user=request.user)
    profile.shop += 1
    profile.save()
    return render(request, 'app/shopping.html')


def earth(request):
    profile = Profile.objects.get(user=request.user)
    profile.compost += 1
    profile.save()
    return render(request, 'app/earth.html')


def car(request):
    global start
    start = time.time()
    return render(request, 'app/car_bg.html')


def scooter(request):
    global start
    start = time.time()
    return render(request, 'app/scooter_bg.html')


def cab(request):
    global start
    start = time.time()
    return render(request, 'app/cab_bg.html')


def rickshaw(request):
    global start
    start = time.time()
    return render(request, 'app/rickshaw_bg.html')


def bus(request):
    global start
    start = time.time()
    return render(request, 'app/bus_bg.html')


def cycle(request):
    global start
    start = time.time()
    return render(request, 'app/cycle_bg.html')


def walking(request):
    global start
    start = time.time()
    return render(request, 'app/walking_bg.html')


def train(request):
    global start
    start = time.time()
    return render(request, 'app/train_bg.html')


def flight(request):
    global start
    start = time.time()
    return render(request, 'app/flight_bg.html')


def endride(request):
    end = time.time()
    profile = Profile.objects.get(user=request.user)
    profile.journey_time = (end - start)/3600
    print(end - start)
    profile.save()
    return render(request, 'app/endride.html')


def carbonfootprint(request):
    profile = Profile.objects.get(user=request.user)
    profile.footprint = 0
    #profile.journey_time = 3600 * 3
    #profile.shop = 0
    #profile.compost = 1
    #profile.solar = 2
    #profile.meal = 5
    #profile.points = 0

    profile.footprint += (profile.electricity / profile.family) * 0.0283
    if profile.diet == 1:
        profile.footprint += profile.meal * 4.988
    elif profile.diet == 2:
        profile.footprint += profile.meal * 4.475
    elif profile.diet == 3:
        profile.footprint += profile.meal * 4.156
    elif profile.diet == 4:
        profile.footprint += profile.meal * 3.93
    elif profile.diet == 5:
        profile.footprint += profile.meal * 3.866
    elif profile.diet == 6:
        profile.footprint += profile.meal * 3.5667
    else:
        profile.footprint += 0

    profile.time = profile.journey_time / 3600
    if profile.car_fuel == 0:
        profile.footprint += profile.time * 6.99
    elif profile.car_fuel == 1:
        profile.footprint += profile.time * 8.04
    elif profile.car_fuel == 2:
        profile.footprint += profile.time * 5.2
    else:
        profile.footprint += 0

    profile.footprint += profile.shop * 1.4

    profile.footprint -= profile.solar * 2.6

    profile.footprint -= profile.compost * 0.05

    profile.footprint += 3

    profile.points = 60000 - (profile.footprint * 1000)

    profile.save()


def solar(request):
    profile = Profile.objects.get(user=request.user)
    profile.solar += 1
    profile.save()
    return render(request, 'app/solar_panel.html')


def output(request):
    profile = Profile.objects.get(user=request.user)
    profile.footprint = 0
    profile.points = 0
    #profile.journey_time = 3600 * 3
    #profile.shop = 0
    #profile.compost = 1
    #profile.solar = 2
    #profile.meal = 5
    profile.electricity = 97

    profile.footprint += (profile.electricity / profile.family) * 0.0283
    if profile.diet == 1:
        profile.footprint += profile.meal * 4.988
    elif profile.diet == 2:
        profile.footprint += profile.meal * 4.475
    elif profile.diet == 3:
        profile.footprint += profile.meal * 4.156
    elif profile.diet == 4:
        profile.footprint += profile.meal * 3.93
    elif profile.diet == 5:
        profile.footprint += profile.meal * 3.866
    elif profile.diet == 6:
        profile.footprint += profile.meal * 3.5667
    else:
        profile.footprint += 0

    profile.time = profile.journey_time / 3600
    if profile.car_fuel == 0:
        profile.footprint += profile.time * 6.99
    elif profile.car_fuel == 1:
        profile.footprint += profile.time * 8.04
    elif profile.car_fuel == 2:
        profile.footprint += profile.time * 5.2
    else:
        profile.footprint += 0

    profile.footprint += profile.shop * 1.4

    profile.footprint -= profile.solar * 2.6

    profile.footprint -= profile.compost * 0.05

    profile.footprint += 3

    profile.points = 60000 - (profile.footprint * 1000)

    context = {'profile': profile}

    profile.save()
    return render(request, 'app/output.html', context)


def statistics(request):
    return render(request, 'app/statistics.html')
