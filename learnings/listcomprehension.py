movies = [
    "Men in Black",
    "Beasts of the nation",
    "Super Man",
    "Before Sunrise",
    "After" "Before Sunset",
    "Sniper",
]

smovies = []
for title in movies:
    if title.startswith("S"):
        smovies.append(title)
print("Using Lists", smovies)


bmovies = [title for title in movies if title.startswith("B")]
print("Using list comprehension:", bmovies)


tracks = [
    ("Killer Queen", 1992),
    ("Bohemian Rhapsody", 1990),
    ("Agar Tum Sath ho", 2010),
    ("Can't help falling in love", 2010),
]

oldmovies = [title for (title, year) in tracks if year < 2000]
print("Old Movies:", oldmovies)

square = [x * x for x in [1, 2, 3, 4, 5]]
print("Squared:", square)
