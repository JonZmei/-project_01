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

# Да, но можно считать не вручную конечно)
# Решение с помощью индекции строк

first_song = my_favorite_songs [
    : my_favorite_songs.find(',')
]

last_song = my_favorite_songs [
    my_favorite_songs.rfind('N') :
]

second_song = my_favorite_songs[
     my_favorite_songs.find('S') : 
     my_favorite_songs.find(', A')
]

previous_song = my_favorite_songs [
    my_favorite_songs.rfind('St') : 
    my_favorite_songs.rfind(', N')
    ]

print(first_song, last_song, second_song, previous_song)


# Решение с помощью метода split() и индексации списков
songs = my_favorite_songs.split(', ')

print(songs[0], songs[-1], songs[1], songs[-2])
