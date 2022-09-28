#!/bin/python
"""
Written by Atissonoun - Credits to MFC & HAC
***You need to initialize the script in order to fix the import and the dependency.
This is only a Beta version of the project***
This python file works as the engine for the project.
imports, coordinates, run......
"""

#Importing modules
import requests
#defining a Api_Keys

Google_API_KEY="Your google API Key goes here"
OpenCell_Api_Key ="Your OpenCellID API Key goes here"

def Google(MMC,MNC,LAC,ID,API_KEY=Google_API_KEY):
    url = "https://www.googleapis.com/geolocation/v1/geolocate?key={}".format(API_KEY)
    data={
    "radioType": "gsm",
    "cellTowers":[
        {
        "cellId": ID,
        "locationAreaCode": LAC,
        "mobileCountryCode": MMC,
        "mobileNetworkCode": MNC
        }
    ]
    }
    response = requests.post(url, json=data)
    if response.status_code == 200 :
        lat=response.json()[u'location'][u'lat']
        long = response.json()[u'location'][u'lng']
        d={'LAT':lat,'LONG':long}
        print('Located Cell: {}'.format(ID))
        return d
    else:
        print('Error: {}'.format(response.status_code))
        return None

def Opencell(MMC,MNC,LAC,ID,API_KEY=OpenCell_Api_Key):
    url = "https://us1.unwiredlabs.com/v2/process.php"
    data = {
        "token": API_KEY,
        "radio": "gsm",
        "mcc": MMC,
        "mnc": MNC,
        "cells": [{
            "lac": LAC,
            "cid": ID
        }]
    }
    response = requests.post(url, json=data)
    if response.status_code == 200:
        if response.json()[u'status']== 'error':
            print('Error: {}'.format(response.json()[u'message']))
            return None
        else:
            lat = response.json()[u'lat']
            long = response.json()[u'lon']
            d = {'LAT': lat, 'LONG': long}
            print('Located Cell: {}'.format(ID))
            return d
    else:
        print('Error: {}'.format(response.status_code))
        return None
