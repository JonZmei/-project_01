my_favorite_songs = "Stairway to Heaven, Imagine, Smells Like Teen Spirit, Bohemian Rhapsody, Hotel California"

# первый трек
print(my_favorite_songs[:18])

# последний трек
print(my_favorite_songs[-16:])

# второй трек
second_track_start = my_favorite_songs.index(", ") + 2
second_track_end = my_favorite_songs.index(", ", second_track_start)
print(my_favorite_songs[second_track_start:second_track_end])

# второй с конца трек
penultimate_track_end = my_favorite_songs.rindex(", ")
penultimate_track_start = my_favorite_songs.rindex(", ", 0, penultimate_track_end) + 2
print(my_favorite_songs[penultimate_track_start:penultimate_track_end])
