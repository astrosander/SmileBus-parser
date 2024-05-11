import Utilities
import telebot

TOKEN = "YourToken"
CHAT_ID = "YourToken"

bot = telebot.TeleBot(TOKEN)

id_city_from = 3    #Mazyr
id_city_to = 1      #Minsk

BaseUrl = f"https://smilebus.by/api/v2/route/schedule-detail?id_city_from={id_city_from}&id_city_to={id_city_to}&date="

dates = [           #dates to parse
    "13.05.2024",
    "14.05.2024",
    "15.05.2024",
]

def send_notification(message):
	bot.send_message(CHAT_ID, message)


if __name__ == "__main__":
    send_notification("Ich arbeite")
    Utilities.monitor_file_changes(dates, BaseUrl)