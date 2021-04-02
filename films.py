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


# function to check if an actor appears in a list of films
# return True if they do, False if they don't
def check_films_for_actor(list_of_films):

    # ask user for the actor to find
    actor_to_find = input("Who are you looking for? ")
    
    # loop through films
    # for each film:
    for film in list_of_films:
        # check stars and costars for actor
        # if we find the actor
            # checking equality for star because film["star"] is a string
            # checking "in" for costars because film["costars"] is a list
        if film["star"] == actor_to_find or actor_to_find in film["costars"]:
        # if actor_to_find in (film["star"], film["costars"]):
            # return True
            return True
        
    # if we don't find the actor in any film
    # return False
    return False


did_we_find_them = check_films_for_actor(films)
print(did_we_find_them)