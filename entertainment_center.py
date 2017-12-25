# movie titles, descriptions, ratings, and posters were aquired from imdb.com
from fresh_tomatoes import open_movies_page
from media import Movie

# the list of movies
MOVIES = [
    Movie(
        "Jumanji: Welcome to the Jungle",
        """Four teenagers discover an old video game
            console and are literally drawn
            into the game's jungle setting, becoming
            the adult avatars they choose.""",
        "PG-13",
        "https://i.imgur.com/qoUkjcT.jpg",
        "https://www.youtube.com/watch?v=2QKg5SZ_35I"),
    Movie(
        "The Greatest Showman",
        """Inspired by the imagination of P.T. Barnum,
            The Greatest Showman is an original musical
            that celebrates the birth of show business
            and tells of a visionary who rose from nothing
            to create a spectacle that became a worldwide sensation.""",
        "PG",
        "https://i.imgur.com/DZp2ITx.jpg",
        "https://www.youtube.com/watch?v=AXCTMGYUg9A"),
    Movie(
        "Pitch Perfect 3",
        """Following their win at the world championship,
            the now separated Bellas reunite for one last
            singing competition at an overseas USO tour,
            but face a group who uses both instruments and voices.""",
        "PG-13",
        "https://i.imgur.com/0nVmra7.jpg",
        "https://www.youtube.com/watch?v=qZkuyLsN3gM")
]

open_movies_page(MOVIES)
