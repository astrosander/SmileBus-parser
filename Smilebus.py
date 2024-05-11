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
    "13.05.2024",
    "14.05.2024",
    "15.05.2024",
]
DatesNum = len(dates)

previous_content = [
    "13.05.2024",
    "14.05.2024",
    "15.05.2024",
]

bot = telebot.TeleBot(TOKEN)

def send_notification(message):
	print(message)
	bot.send_message(CHAT_ID, message)


def CompareStr(s1, s2):
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            if (int(s2[i]) - int(s1[i]) > 0):
                return f"Number of seats for {s1[i+10:i+15]} has changed {s1[i]} -> {s2[i]}"
            return f"One seat was taken. Total number of seats: {s2[i]}"

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
            return str(soup)#.encode('utf-8').decode('unicode_escape')
        else:
            print("Failed to retrieve HTML content. Status code:", response.status_code)
    except Exception as e:
        print("An error occurred:", e)
    return None



def monitor_file_changes():

    for i in range(len(dates)):
        previous_content[i] = read_file_content(dates[i])

    while True:
        for i in range(len(dates)):
            current_content = read_file_content(dates[i])

            if current_content != previous_content[i]:
                send_notification(f"⚠️An update detected for {dates[i]}\n{CompareStr(previous_content[i], current_content)}" )
                previous_content[i] = current_content
            

			

if __name__ == "__main__":
    send_notification("Ich arbeite")
    monitor_file_changes()
