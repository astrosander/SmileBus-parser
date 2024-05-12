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
  '33' Светлогорск
  '34' Речица
  '35' Скалка
  '36' Прудок
  '37' Судовица поворот
  '38' Ракшин
  '39' Стужки поворот
  '40' Чирковичи
  '41' Медков
  '42' Боровики речица
  '43' Узнож-Заходы перекресток
  '44' Заречье поворот
  '45' Старокрасная
  '46' Новокрасная
  '47' Гомель
  '48' Плессы
  '49' Новый Остров
  '50' Белица
  '51' Лебедевка
  '52' Губичи
  '53' Недойка
  '54' Кривск
  '55' Житовля
  '56' Стар Белица-Урицкое перекрест
  '57' Михайловка-Раковичи перекрест
  '58' Рогачев
  '59' Кобрин
  '60' Наспа
  '61' 14-й километр
  '62' Долгорожская Слобода
  '63' Борщевка1
  '64' Барак
  '65' Рынья
  '66' Большие бортники
  '67' Пересека
  '68' Дворец
  '69' Лисковская слобода
  '70' Смольное
  '71' Ямное
  '72' Кошара
  '73' Гусаровка
  '74' Стреньки
  '120' Жлобин
  '127' Боец
  '129' Турки
  '130' Ковали
  '131' Поворот на Солтаново
  '133' д. Веселое
  '134' Веселое 
  '135' Илосск
  '136' Новоселки
  '137' Черкасы
  '138' Чечино
  '139' Вязань
  '140' Веста
  '141' Лоев
  '142' Брагин
  '143' Хойники
  '144' Козелужье
  '145' Вить
  '146' Слобожанка
  '147' Алексичи
  '148' Рабец
  '149' Глинище
  '150' Боец трасса Р35
  '151' Ельск
  '152' Лельчицы
  '153' Княжеборье поворот
  '154' Санюки
  '155' Мазуры
  '156' Рудня Р31
  '157' Пеньки
  '158' Раевские
  '159' Бобренята
  '160' Новики
  '161' Липляны
  '162' Буда-Лельчицкая
  '163' Краснобережье
  '164' Буйновичи
  '165' Буда-Софиевка
  '166' Махновичи
  '167' Ремезы
  '168' Движки
  '169' Глуск
  '170' Октябрьский
  '171' Наровля
  '176' Дербин
  '177' Волосовичи
  '178' Нестановичи
  '180' Гать
  '182' Холопеничи
  '183' Катка
  '186' Погорелое
  '189' Вильча1
  '236' Спорное
  '238' Карповичи
  '239' Поворот на Жолвинец
  '240' Кировское
  '241' Поворот на Заречье
  '337' Поворот на Тихиничи
  '338' Брест
  '339' Симоничский Млынок
  '340' Симоничи
  '341' Средние печи
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
