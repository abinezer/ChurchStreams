from django.http import HttpResponse
from django.shortcuts import render
import requests
import json

def index(request):
    #return HttpResponse("Hello, world. You're at the polls index.")
    pattern = "This video is unavailable"
    with open('data.json') as json_file:
        Channels = json.load(json_file)
    listOfVideos = []
    for i in Channels.keys():
        r = requests.get("https://www.youtube.com/embed/live_stream?channel={}".format(Channels[i]))
        if pattern not in r.text:
            listOfVideos.append({'link':"https://www.youtube.com/embed/live_stream?channel={}".format(Channels[i]),
                                 'title': i})
    return render(request, 'homepage.html',{'listOfVideos':listOfVideos})
