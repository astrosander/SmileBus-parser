import os
import time
import telebot

import requests
from bs4 import BeautifulSoup


TOKEN = "YourToken"
CHAT_ID = "YourToken"

id_city_from = 3    #Mazyr
id_city_to = 1      #Minsk

dates = [#dates to parse
    "10.05.2024",
    "11.05.2024",
    "12.05.2024",
    "13.05.2024",
    "14.05.2024",
    "15.05.2024",
    "16.05.2024",
    "17.05.2024",
    "18.05.2024",
    "19.05.2024",
    "20.05.2024",
    "21.05.2024",
    "22.05.2024",
    "23.05.2024",
    "24.05.2024"
]
DatesNum = len(dates)

previous_content = [
    "10.05.2024",
    "11.05.2024",
    "12.05.2024",
    "13.05.2024",
    "14.05.2024",
    "15.05.2024",
    "16.05.2024",
    "17.05.2024",
    "18.05.2024",
    "19.05.2024",
    "20.05.2024",
    "21.05.2024",
    "22.05.2024",
    "23.05.2024",
    "24.05.2024"
]

bot = telebot.TeleBot(TOKEN)

def send_notification(message):
	print(message)
	bot.send_message(CHAT_ID, message)


def read_file_content(date):
    url = (
        f"https://smilebus.by/api/v2/route/schedule-detail?id_city_from={id_city_from}&id_city_to={id_city_to}&date={date}"
    )
    time.sleep(2)

    try:
        response = requests.get(url)
        if response.status_code == 200:
            html_content = response.text
            soup = BeautifulSoup(html_content, "html.parser")
            return str(soup)
        else:
            print("Failed to retrieve HTML content. Status code:", response.status_code)
    except Exception as e:
        print("An error occurred:", e)
    return None


def monitor_file_changes():

    for i in range(DatesNum):
    	previous_content[i] = read_file_content(dates[i])

    while True:
    	for i in range(len(dates)):
		    current_content = read_file_content(dates[i])

		    if current_content != previous_content[i]:
		        send_notification("⚠️A new trip showed up for " + str(dates[i]))
		        previous_content[i] = current_content
			

if __name__ == "__main__":
    monitor_file_changes()
