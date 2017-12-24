#entertainment_center.py
#movie titles, descriptions, ratings, and posters were aquired from imdb.com
from fresh_tomatoes import open_movies_page
from media import Movie

#the list of movies 
MOVIES = [
	Movie("Jumanji: Welcome to the Jungle", 
		"Four teenagers discover an old video game console and are literally drawn into the game's jungle setting, becoming the adult avatars they choose.", 
		"PG-13", 
		"https://images-na.ssl-images-amazon.com/images/M/MV5BMTkyNDQ1MDc5OV5BMl5BanBnXkFtZTgwOTcyNzI2MzI@._V1_.jpg", 
		"https://www.youtube.com/watch?v=2QKg5SZ_35I"),
	Movie("The Greatest Showman", 
		"Inspired by the imagination of P.T. Barnum, The Greatest Showman is an original musical that celebrates the birth of show business and tells of a visionary who rose from nothing to create a spectacle that became a worldwide sensation.", 
		"PG", 
		"https://images-na.ssl-images-amazon.com/images/M/MV5BYjQ0ZWJkYjMtYjJmYS00MjJiLTg3NTYtMmIzN2E2Y2YwZmUyXkEyXkFqcGdeQXVyNjk5NDA3OTk@._V1_SY1000_SX675_AL_.jpg", 
		"https://www.youtube.com/watch?v=AXCTMGYUg9A"),
	Movie("Pitch Perfect 3", 
		"Following their win at the world championship, the now separated Bellas reunite for one last singing competition at an overseas USO tour, but face a group who uses both instruments and voices.", 
		"PG-13", 
		"https://images-na.ssl-images-amazon.com/images/M/MV5BNjEyMjk4NTE1NV5BMl5BanBnXkFtZTgwOTgzNzA3MjI@._V1_SY1000_CR0,0,631,1000_AL_.jpg", 
		"https://www.youtube.com/watch?v=qZkuyLsN3gM")
]

open_movies_page(MOVIES)