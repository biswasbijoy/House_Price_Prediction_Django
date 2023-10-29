from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import pickle
import json
import numpy as np


def prediction(request):
    return render(request, 'prediction.html')


__locations = None
__data_columns = None
__model = None


def columns():
    global __data_columns
    global __locations
    with open("columns.json", "r") as f:
        __data_columns = json.load(f)['data_columns']
        __locations = __data_columns[3:]
    global __model
    if __model is None:
        with open('model.pickle', 'rb') as f:
            __model = pickle.load(f)


def get_location_names():
    columns()
    return __locations


def location(request):
    columns()
    res = get_location_names()
    print(res)
    return JsonResponse({"area_names": res})


def get_data_columns():
    columns()
    return __data_columns


def util(location, sqft, bhk, bath):
    columns()
    try:
        loc_index = __data_columns.index(location.lower())
    except:
        loc_index = -1

    x = np.zeros(len(__data_columns))
    x[0] = sqft
    x[1] = bath
    x[2] = bhk
    if loc_index >= 0:
        x[loc_index] = 1

    return round(__model.predict([x])[0], 2)


def prediction_result(request):
    location = request.GET['location']
    area = float(request.GET['area'])
    bedroom = float(request.GET['bedroom'])
    bathroom = float(request.GET['bathroom'])

    ans = util(location, area, bedroom, bathroom)
    area = location
    return render(request, 'prediction.html', {'area': area, 'ans': ans})
    # model = pickle.load(open('/home/bijoy-404/Django/myhome/myhome/predict/saved_model/model.pickle', 'rb'))
    #
    # var1 = request.GET['location']
    # var2 = float(request.GET['area'])
    # var3 = float(request.GET['bathroom'])
    # var4 = float(request.GET['bedroom'])
    # ans = model.predict('Mirsharai', 1600, 3,3)
    # return render(request, 'prediction.html', {'ans': ans})
