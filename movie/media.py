import webbrowser

class Movie():
    def __init__(self, title, storyline, poster_image_url, trailer_youtube_url, ranking):
        self.title = title
        self.storyline = storyline
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url
        self.ranking = ranking

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
