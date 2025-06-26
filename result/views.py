from django.shortcuts import render
import pickle
import pandas as pd
#import numpy as np
from django.http import HttpResponse



country_dict = {
    0: 'Algeria', 1: 'Angola', 2: 'Argentina', 3: 'Australia', 4: 'Azerbaijan',
    5: 'Bangladesh', 6: 'Brazil', 7: 'Bulgaria', 8: 'Burkina Faso', 9: 'Burundi',
    10: 'Cameroon', 11: 'Canada', 12: 'Central African Republic', 13: 'Chile',
    14: 'Colombia', 15: 'Croatia', 16: 'Dominican Republic', 17: 'Ecuador',
    18: 'Egypt', 19: 'El Salvador', 20: 'France', 21: 'Germany', 22: 'Ghana',
    23: 'Greece', 24: 'Guatemala', 25: 'Guinea', 26: 'Guyana', 27: 'Haiti',
    28: 'Honduras', 29: 'Hungary', 30: 'India', 31: 'Indonesia', 32: 'Iraq',
    33: 'Italy', 34: 'Jamaica', 35: 'Japan', 36: 'Kazakhstan', 37: 'Kenya',
    38: 'Libya', 39: 'Madagascar', 40: 'Malawi', 41: 'Mali', 42: 'Mauritania',
    43: 'Mauritius', 44: 'Mexico', 45: 'Morocco', 46: 'Mozambique', 47: 'Nepal',
    48: 'Nicaragua', 49: 'Niger', 50: 'Pakistan', 51: 'Papua New Guinea', 52: 'Peru',
    53: 'Portugal', 54: 'Romania', 55: 'Rwanda', 56: 'Saudi Arabia', 57: 'Senegal',
    58: 'South Africa', 59: 'Spain', 60: 'Sri Lanka', 61: 'Suriname', 62: 'Tajikistan',
    63: 'Thailand', 64: 'Turkey', 65: 'Uganda', 66: 'Ukraine', 67: 'United Kingdom',
    68: 'Uruguay', 69: 'Zambia', 70:'Zimbabwe'
}

item_dict = {
    0: 'Maize', 1: 'Potatoes', 2: 'Rice, paddy', 3: 'Sorghum', 4: 'Wheat',
    5: 'Cassava', 6: 'Sweet potatoes', 7: 'Soybeans', 8: 'Yams',
    9: 'Plantains and others'
}
# Create your views here.
def cropResult(request):
    model = pickle.load(open('../models/random_forest_model.pkl', 'rb'))
    result = 'Some error has occured'
    if (request.method == 'POST'):
        # result = 'shrut'
        string_Area = (request.POST.get('area'))
        Area = country_dict.get(string_Area)
        Item = (request.POST.get('item'))
        Item = item_dict.get(Item)
        Year = int(request.POST.get('year'))
        average_rain_fall_mm_per_year = float(request.POST.get('average_rain_fall_per_mm'))
        pesticides_tonnes = float(request.POST.get('pesticide_tonnes'))
        avg_temp = float(request.POST.get('avg_temp'))
        print(type(Area),type(Item), type(Year),type(average_rain_fall_mm_per_year),type(pesticides_tonnes),type(avg_temp))
        
        prop = []
        prop.extend([Area, Item, Year, average_rain_fall_mm_per_year, pesticides_tonnes, avg_temp])
        prop_data = pd.DataFrame(columns=['Area', 'Item', 'Year', 'average_rain_fall_mm_per_year', 'pesticides_tonnes', 'avg_temp'])
        prop_data.loc[len(prop)] = prop
        result = model.predict(prop_data)
    print(result)
    return render(request , 'result.html' , {'result' : result})
    # return HttpResponse(str(result))

def home(request):
    return render(request,'index.html')
