# SmileBus-parser

<p align="center">
  <br>
  <img src="https://github.com/astrosander/SmileBus-parser/assets/69795340/e53b425d-5015-41d4-80e9-1b000d8d6341" width="360"/><br><br>
 <b>Parser to track new seats at SmileBus transport company</b><br><br>
</p>
<p>
  🚌Parser for tracking the appearance of new seats in the Smilebus app and sending notifications through Telegram Bot


## Python Installation <img align="center"  width="28px" src="https://github.com/astrosander/WallTime/blob/main/Themes/snakes.png" />

You can install the tool using Python. 
Download or clone the GitHub repository and install the necessary requirements with:

```sh
pip install -r requirements.txt
```

## Launch the Scraper:

Initially, in the file `Smilebus.py` change constant values:

`TOKEN` and `CHAT_ID` - the ones you got through bot registration

`id_city_from` and `id_city_to` - id of departure and destination places  

<details>
  <summary><h2>🌆List of station IDs</h2></summary>
  
  ### 

  <pre>
  '1' Минск
  '2' Калинковичи
  '3' Мозырь
  '4' Привольный
  '5' Хозянинки
  '6' Дукора
  '7' Марьина горка (Затишье)
  '8' Пуховичи
  '9' Теплухи Осиповичи
  '10' Ясень
  '11' Бояры
  '12' Брожка
  '13' Вишневка поворот
  '14' Красновка
  '15' Михайловка
  '16' Паричи
  '17' Козловка
  '18' Песчаная рудня поворот
  '19' Селищи
  '20' Памятник опер Багратион
  '20' Ясень
  '21' Дуброва
  '22' Полесье
  '23' Лесец
  '24' Озаричи
  '25' Козловичи
  '26' Домановичи поворот
  '27' Сельцы
  '28' Бобровичи поворот
  '29' Туровичи - Булавки перекресток
  '30' Дудичи
  '31' Ситня
  </pre>

</details>


`dates` - dates you want to parse

For instance:

```sh
dates = [          
    "13.05.2024",
    "14.05.2024",
    "15.05.2024",
]
```


Compile `Smilebus.py` 

## Usage:

After launching, every change in number of seats would be detected and you will be informed immediately through Telegram bot.

<p align="left">
  <br>
  <img src="https://github.com/astrosander/SmileBus-parser/assets/69795340/58e4c2d3-992c-42fa-bb68-72ee6e36a5d9" width="480"/><br><br>
</p>

<details>
  <summary><h2>How to create a bot in Telegram <img align="center"  width="40px" src="https://github.com/astrosander/LEDeffects/blob/main/Design/bot_father.png" /></h2> </summary>
  
  1. You must have telegram
  2. Go to <a href="https://t.me/BotFather">@BotFather</a>
  3. Send ```/newbot```
  4. Then, send name You woud like to choose(Ex.: ```AstroLamp```)
  5. Send send *username*(Ex.: ```astrolamp_bot```)
  6. All right, You just created Your own bot!
</details>
<details>
  <summary><h2>How to get my Telegram ID <img align="center"  width="35px" src="https://github.com/astrosander/LEDeffects/raw/main/Design/myid.jpg" /> </h2> </summary>
  
  1. You must have telegram
  2. Go to <a href="https://t.me/myidbot">@IDBot</a>
  3. Send ```/getid```
  4. Copy Your id!
</details>

##  Plans for future📜

🔹Make a brief summary about available seats 💺

🔹Make a full statistics of available seats over a period of time ⏳
