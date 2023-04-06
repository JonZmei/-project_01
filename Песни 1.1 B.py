import random
import datetime

my_favorite_songs_dict = {
    "Потеряй минутку": 3.03,
    "Новое спасение": 4.02,
    "Остаться в живых": 3.40,
    "Вне связи": 3.03,
    "Своего рода сказка": 5.28,
    "Легко": 4.15,
    "Прекрасный день": 4.04,
    "Некуда бежать": 2.58,
    "В этом мире": 4.02,
}

# Генерация трех случайных песен
random_songs = random.sample(list(my_favorite_songs_dict.keys()), 3)

# Подсчет общего времени звучания
total_time = sum([my_favorite_songs_dict[song] for song in random_songs])

# Перевод общего времени в формат времени
total_time_formatted = str(datetime.timedelta(minutes=total_time))

print("Три песни звучат {} минут.".format(total_time_formatted))

# Отличное решение
