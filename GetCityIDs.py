import requests
from bs4 import BeautifulSoup
import time
import json 

id_city_to = 2      #Minsk

bool_list = [False] * 500

def read_file_content(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            html_content = response.text
            soup = BeautifulSoup(html_content, "html.parser")
            return str(soup)
  
    except Exception as e:
        pass

def analyze_string(input_string):
    try:
        cities = json.loads(input_string)

        stops = f"'{cities['stops_start'][0]['id_city']}'{cities['stops_start'][0]['city_name']}"
        
        if bool_list[int(cities['stops_start'][0]['id_city'])] == False:
            print(stops)

        if int(cities['stops_start'][0]['id_city']) > 0 and int(cities['stops_start'][0]['id_city']) < 500:
            bool_list[int(cities['stops_start'][0]['id_city'])] = True

    except Exception as e:
        pass


for j in range (1,350):
    for i in range (1,350):
        try:
            str2 = read_file_content(f"https://smilebus.by/api/v2/route/schedule-detail?id_city_from={i}&id_city_to={j}&date=18.05.2024").encode('utf-8').decode('unicode_escape')
            analyze_string(str2)
        except Exception as e:
            pass