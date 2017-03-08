# Lesson 3.4: Make Classes
# Mini-Project: Movies Website

# In this file, you will define instances of the class Movie defined
# in media.py. After you follow along with Kunal, make some instances
# of your own!

# After you run this code, open the file fresh_tomatoes.html to
# see your webpage!

import media
import fresh_tomatoes

the_big_short = media.Movie("The Big Short", "WS",  "https://upload.wikimedia.org/wikipedia/en/e/e3/The_Big_Short_teaser_poster.jpg", "https://youtu.be/O1X0KDdS5Bw")

movies = [the_big_short]
fresh_tomatoes.open_movies_page(movies)
