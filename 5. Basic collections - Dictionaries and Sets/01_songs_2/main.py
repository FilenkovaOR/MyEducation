violator_songs = {
    'World in My Eyes': 4.86,
    'Sweetest Perfection': 4.43,
    'Personal Jesus': 4.56,
    'Halo': 4.9,
    'Waiting for the Night': 6.07,
    'Enjoy the Silence': 4.20,
    'Policy of Truth': 4.76,
    'Blue Dress': 4.29,
    'Clean': 5.83
}


sum_minutes = 0
amt_songs = int(input("Сколько песен выбрать? "))

for i in range(1, amt_songs + 1):
    name_song = input("Название {}-ой песни: ".format(i))
    if name_song in violator_songs:
        sum_minutes += violator_songs[name_song]

print("Общее время звучания песен:", sum_minutes)



