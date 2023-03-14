import random
import datetime

my_favorite_songs = [
    ["Потеряй мгновение", 3.03],
    ["Новое спасение", 4.02],
    ["Остаться в живых", 3.40],
    ["Вне связи", 3.03],
    ["Своего рода сказка", 5.28],
    ["Легко", 4.15],
    ["Прекрасный день", 4.04],
    ["Некуда бежать", 2.58],
    ["В этом мире", 4.02]
]

# Выберем три случайные песни из списка
random_songs = random.sample(my_favorite_songs, 3)

# Посчитаем общее время звучания трех песен
total_time = sum(song[1] for song in random_songs)

# Выведем результат на экран
print(f"Три песни звучат {total_time:.0f} минут")
