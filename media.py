#media.py

class Movie():
	#initialize the movie object with the required content
	def __init__(self, title, desc, rating, p_url, yt_url):
		self.title = title
		self.description = desc 
		self.poster_image_url = p_url
		self.trailer_youtube_url = yt_url
		self.set_valid_rating(rating)

	#this function ensures a valid rating is entered, also, empty
	def set_valid_rating(self, rating):
		try: 
			self.get_valid_ratings().index(rating)#this will throw an exception if rating is not in the list of valid ratings
			self.rating = rating#sets the valid rating 
		except ValueError:# either rating is not specified or the rating is not valid
			print("No valid rating was entered for " + title);
			self.rating = "NR"# NR for Not-Rated

	def get_valid_ratings(self):
		return ["G", "PG", "PG-13", "R"]