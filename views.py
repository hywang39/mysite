#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse

from delivery.models import Restaurant

from .forms import RestaurantAdditionForm
from .forms import RestaurantAdvanceForm
from .models import DBVersion
from django.http import HttpResponseRedirect


from pytube import YouTube
import subprocess

# Create your views here.
import json
import time


def index(request):
    return render(request, template_name='delivery/index.html');


def home(request):
    return render(request, template_name='delivery/home.html');


def deliveryAdmin(request):
    def loadRestaurantListIntoJson(allRest):
        dict = {}
        for restaurant in allRest:
            dict[restaurant.restaurant_name] = restaurant.restaurant_id
        js_data = json.dumps(dict)
        dict = {}
        return js_data

    allrestaurant = Restaurant.objects.all()
    js_data = loadRestaurantListIntoJson(allrestaurant)

    # if a GET (or any other method) we'll create a blank form
    # elif request.method == 'GET':
    #     restID = request.GET['id']
    #     selectedRestaurant = Restaurant.objects.get(pk=restID);
    #     dict = {}
    #     # for field in selectedRestaurant:
    #     #     dict[field] = selectedRestaurant.
    #
    #     return HttpResponse("")

    form = RestaurantAdditionForm()
    return render(request, 'delivery/deliveryAdmin.html', {'form': form, 'data': js_data})
    # return render(request, 'delivery/deliveryAdmin.html', {'form': form, 'data': 'lalala'})

    # 'rest2name':query_results.restaurant_name


def restAdvanceInfo(request):
    form = RestaurantAdvanceForm()
    restID = request.GET['id']
    selectedRestaurant = Restaurant.objects.get(pk=restID);

    if request.method == 'GET':
        return render(request, 'delivery/advanceinfo.html', {'form': form, 'rest': selectedRestaurant, })

    else:

        selectedRestaurant.restaurant_name = request.POST.get('restaurant_name')
        selectedRestaurant.restaurant_address = request.POST.get('restaurant_address')
        selectedRestaurant.restaurant_category_id = request.POST.get('restaurant_category_id')
        selectedRestaurant.restaurant_description = request.POST.get('restaurant_description')
        selectedRestaurant.restaurant_phone = request.POST.get('restaurant_phone')
        selectedRestaurant.restaurant_email = request.POST.get('restaurant_email')

        selectedRestaurant.save()
        return HttpResponseRedirect('/deliveryadmin/')


def deleteRestaurant(request):
    restID = request.GET.get('restID')
    selectedRestaurant = Restaurant.objects.get(pk=restID)
    selectedRestaurant.delete()
    return HttpResponse(json.dumps({'message': 'delete_success'}))


def addRestaurant(request):
    if request.method == 'POST':

        # create a form instance and populate it with data from the request:
        form = RestaurantAdditionForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:

            rest = Restaurant()
            rest.restaurant_name = request.POST.get('restaurant_name')
                # if rest.restaurant_name in Restaurant
            # try:
            #     rest = Restaurant.objects.get(restaurant_name=rest.restaurant_name)
            #     rest = Restaurant()
            # except rest.DoesNotExist:
            rest.restaurant_address = request.POST.get('restaurant_address')
            rest.restaurant_category_id = request.POST.get('restaurant_category_id')
            rest.restaurant_description = request.POST.get('restaurant_description')
            rest.restaurant_phone = request.POST.get('restaurant_phone')
            rest.restaurant_email = request.POST.get('restaurant_email')
            dbVersion = DBVersion.objects.last()
            dbVersion.minor_version += 1
            dbVersion.save()
            rest.save()
            rest = Restaurant.objects.all().last()

            # if (rest.restaurant_id == None):
            #     return HttpResponse(json.dumps({'message': 'DuplicateName'}))
            # else:
            return HttpResponseRedirect('/deliveryadmin/restaurantadvanceinfo?id=' + str(rest.restaurant_id))
                # return HttpResponse(json.dumps({'message': 'add_success'}))


def getAvailability(request):
    restName = request.GET.get('restName')
    if restName !='':
        try:
            restaurant = Restaurant.objects.get(restaurant_name=restName)
            return HttpResponse(json.dumps({'message':'exist'}))
        except restaurant.DoesNotExist:
            return HttpResponse(json.dumps({'message':'nonexist'}))
    else:
        return HttpResponse(json.dumps({'message': 'empty'}))

def youtubedler(request):
    return render(request, 'delivery/youtubedler.html')

def prepare_download(request):
    if request.method == 'GET':

        file_url = request.GET.get('url')
        if (file_url == ""):
            return HttpResponse(json.dumps({'success': 'false'}))
        try:
            yt = YouTube(file_url)
        except:
            return HttpResponse(json.dumps({'success': 'false'}))

	video = yt.filter("mp4")[0]
        video.filename = yt.filename.replace(' ','')

        file_name = video.filename
        path = '/var/djangoprojects/untitled/static/media'
        str_timestamp = str(int(time.time()*1000000))

        command_add_dir = "sudo mkdir -m 777 " +  path + '/' + str_timestamp
        subprocess.call(command_add_dir, shell=True)

        added_path = path + '/' + str_timestamp

        video.download(added_path)


        command_convert = "ffmpeg -i " + added_path+ '/' + '\'' + file_name + ".mp4" + '\'' + " -ab 160k -ac 2 -ar 44100 -vn "+ added_path+ '/' + '\'' +file_name + ".mp3" + '\''
        subprocess.call(command_convert, shell=True)

        dict = {'success': 'true', 'str_timestamp': str_timestamp, 'file_name' : file_name + '.mp3'}
        return HttpResponse(json.dumps(dict))
