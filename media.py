import webbrowser

class Movie():
    #This class provides a way to store movie related information

    def __init__(self, title, poster_image_url, trailer_youtube_url):
        #initialize instance of class Movie
        self.title = title
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url

    #def play_trailer(self):
        #play the movie trailer
        #webbrower.open(self.trailer_youtube_url)
