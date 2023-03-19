# importing spacy and specifying the model to be used
import spacy
nlp = spacy.load('en_core_web_md')

# takes in a movie description and returns the most similar movie in 'movies.txt' using spacy.similarity
def watch_next(description):

    with open("movies.txt", "r") as f:  
        movies = f.readlines()
        # define reference sentence for the comparison
        reference_sentence = nlp(description)  
        most_similar = 0  
        suggested_movie = ''

        # Loop through all movies from the list and find the most similar title   
        for movie_description in movies:  
            similarity = nlp(movie_description[9:]).similarity(reference_sentence)
            if similarity >= most_similar:
                most_similar = similarity
                suggested_movie = movie_description
    return f"You will probably like '{suggested_movie[:7]}' too!"


# take in the description as a parameter and return the title of the most similar movie.
watched_before = """Will he save their world or destroy it? When the Hulk becomes too dangerous for the Earth, 
the Illuminati trick Hulk into a shuttle and launch him into space to a planet Sakaar where he is sold into slavery 
and trained as a gladiator."""

print(watch_next(watched_before))