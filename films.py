films = [
    {
        "title": "Alien",
        "genre": "sci-fi",
        "rating": 18,
        "star": "Sigourney Weaver",
        "costars": [
            "John Hurt", 
            "Tom Skerrit"
            ]
    },
    {
        "title": "Gladiator",
        "genre": "drama",
        "rating": 15,
        "star": "Russell Crowe",
        "costars": [
            "Joaquin Phoenix", 
            "Connie Nielsen", 
            "Oliver Reed"
            ]
    },
    {
        "title": "Joker",
        "genre": "drama",
        "rating": 15,
        "star": "Joaquin Phoenix",
        "costars": [
            "Robert De Niro"
        ]
    }
]

print(films[0]["costars"][0])

my_film = films[0]

my_costars = my_film["costars"]

first_costar = my_costars[0]

print(first_costar)




print(f'The film {films[0]["title"]} has the genre {films[0]["genre"]}')

# print(films[0]["title"], films[0]["genre"])