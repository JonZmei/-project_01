#Здесь мы использовали индексы, чтобы извлечь нужные части строки my_favorite_songs.
#Для первого трека мы использовали индексы 0:15, чтобы извлечь первые 15 символов строки (то есть название первой песни).
#Для последнего трека мы использовали индексы -18:,
#чтобы извлечь последние 18 символов строки
#(то есть название последней песни)

my_favorite_songs = "Stairway to Heaven, Hotel California, Imagine, Hey Jude, Comfortably Numb"

# первый трек
print(my_favorite_songs[:18])

# последний трек
print(my_favorite_songs[39:])

# второй трек
print(my_favorite_songs[21:38])

# второй с конца трек
print(my_favorite_songs[-22:-5])