import media
import fresh_tomatoes

the_big_short = media.Movie("The Big Short",  \
"https://upload.wikimedia.org/wikipedia/en/e/e3/The_Big_Short_teaser_poster.jpg", "https://youtu.be/O1X0KDdS5Bw")
margin_call = media.Movie("Margin Call", "https://upload.wikimedia.org/wikipedia/en/6/62/Margin_Call.jpg", \
"https://youtu.be/Y2DqFRsPrns")
the_wolf_of_wall_street = media.Movie("The Wolf of Wall Street", \
"https://upload.wikimedia.org/wikipedia/en/1/1f/WallStreet2013poster.jpg", \
"https://youtu.be/iszwuX1AK6A")
pacific_rim = media.Movie("Pacific Rim", \
"https://upload.wikimedia.org/wikipedia/en/f/f3/Pacific_Rim_FilmPoster.jpeg", "https://youtu.be/5guMumPFBag")
godzilla = media.Movie("Godzilla", "https://upload.wikimedia.org/wikipedia/en/1/10/Godzilla_%282014%29_poster.jpg", \
"https://youtu.be/vIu85WQTPRc")
world_war_z = media.Movie("World War Z", "https://upload.wikimedia.org/wikipedia/en/d/dc/World_War_Z_poster.jpg", \
"https://youtu.be/HcwTxRuq-uk")
gravity = media.Movie("Gravity", "https://upload.wikimedia.org/wikipedia/en/f/f6/Gravity_Poster.jpg", \
"https://youtu.be/OiTiKOy59o4")
rush = media.Movie("Rush", "https://upload.wikimedia.org/wikipedia/en/d/d0/Rush_UK_poster.jpeg", \
"https://youtu.be/4XA73ni9eVs")
black_hawk_down = media.Movie("Black Hawk Down", \
"https://upload.wikimedia.org/wikipedia/en/0/0c/Black_hawk_down_ver1.jpg", "https://youtu.be/QjouwbniJSs")

movies = [the_big_short, margin_call, the_wolf_of_wall_street, pacific_rim, godzilla, \
world_war_z, gravity, rush, black_hawk_down]
fresh_tomatoes.open_movies_page(movies)
