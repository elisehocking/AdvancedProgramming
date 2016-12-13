import media
import fresh_tomatoes

broadcity = media.Movie("Broad City", "Broad City follows two women throughout their daily lives in New York City.", "http://www.gstatic.com/tv/thumb/tvbanners/12494895/p12494895_b_v8_aa.jpg","https://www.youtube.com/watch?v=PMIjEnEZTDM", "4.8 out of 5 stars" )
mindy = media.Movie("The Mindy Project", "The Mindy Project stars Mindy Kaling as a skilled OB/GYN navigating the tricky waters of both her personal & professional life.", "http://content.hollywire.com/sites/default/files/2015/07/28/Mindy-Project.jpg", "https://www.youtube.com/watch?v=NCLw0QmEs94", "5 out of 5 stars" )
arrested = media.Movie("Arrested Development", "A son reluctantly tries to save the world's craziest family from themselves.", "http://vignette3.wikia.nocookie.net/arresteddevelopment/images/6/6b/Season_3_square.jpg/revision/latest?cb=20111023065401", "https://www.youtube.com/watch?v=TntmMY7N8ag", "4.6 out of 5 stars")

movies = [broadcity, mindy, arrested]

fresh_tomatoes.open_movies_page(movies)
