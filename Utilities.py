import requests
from bs4 import BeautifulSoup
import time
import Smilebus

def CompareStr(s1, s2):
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            if (int(s2[i]) - int(s1[i]) > 0):
                return f"Number of seats for {s1[i+10:i+15]} has changed {s1[i]} -> {s2[i]}"
            return f"One seat was taken. Total number of seats: {s2[i]}"

def read_file_content(url):
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

def monitor_file_changes(dates, BaseUrl):
	previous_content = []

	for i in range(len(dates)):
		previous_content.append(read_file_content(BaseUrl+dates[i]))

	while True:
		for i in range(len(dates)):
			current_content = read_file_content(BaseUrl+dates[i])

			if current_content != previous_content[i]:
				Smilebus.send_notification(f"⚠️An update detected for {dates[i]}\n{CompareStr(previous_content[i], current_content)}" )
				previous_content[i] = current_content