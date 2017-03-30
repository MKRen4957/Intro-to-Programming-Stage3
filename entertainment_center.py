import media
import fresh_tomatoes

# Create an instance movie "The Big Short"
the_big_short = media.Movie(
    "The Big Short",
    "https://upload.wikimedia.org/wikipedia/en/e/e3/The_Big_Short_teaser_poster.jpg",
    "https://youtu.be/O1X0KDdS5Bw")
# Create an instance movie "Margin Call"
margin_call = media.Movie(
    "Margin Call",
    "https://upload.wikimedia.org/wikipedia/en/6/62/Margin_Call.jpg",
    "https://youtu.be/Y2DqFRsPrns")
# Create an instance movie "The Wolf of Wall Street"
the_wolf_of_wall_street = media.Movie(
    "The Wolf of Wall Street",
    "https://upload.wikimedia.org/wikipedia/en/1/1f/WallStreet2013poster.jpg",
    "https://youtu.be/iszwuX1AK6A")
# Create an instance movie "Pacific Rim"
pacific_rim = media.Movie(
    "Pacific Rim",
    "https://upload.wikimedia.org/wikipedia/en/f/f3/Pacific_Rim_FilmPoster.jpeg",
    "https://youtu.be/5guMumPFBag")
# Create an instance movie "Godzilla"
godzilla = media.Movie(
    "Godzilla",
    "https://upload.wikimedia.org/wikipedia/en/1/10/Godzilla_%282014%29_poster.jpg",
    "https://youtu.be/vIu85WQTPRc")
# Create an instance movie "World War Z"
world_war_z = media.Movie(
    "World War Z",
    "https://upload.wikimedia.org/wikipedia/en/d/dc/World_War_Z_poster.jpg",
    "https://youtu.be/HcwTxRuq-uk")
# Create an instance movie "Gravity"
gravity = media.Movie(
    "Gravity",
    "https://upload.wikimedia.org/wikipedia/en/f/f6/Gravity_Poster.jpg",
    "https://youtu.be/OiTiKOy59o4")
# Create an instance movie "Rush"
rush = media.Movie(
    "Rush",
    "https://upload.wikimedia.org/wikipedia/en/d/d0/Rush_UK_poster.jpeg",
    "https://youtu.be/4XA73ni9eVs")
# Create an instance movie "Black Hawk Down"
black_hawk_down = media.Movie(
    "Black Hawk Down",
    "https://upload.wikimedia.org/wikipedia/en/0/0c/Black_hawk_down_ver1.jpg",
    "https://youtu.be/QjouwbniJSs")

movies = [the_big_short, margin_call, the_wolf_of_wall_street, pacific_rim, godzilla, \
world_war_z, gravity, rush, black_hawk_down]
fresh_tomatoes.open_movies_page(movies)
