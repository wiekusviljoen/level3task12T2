import spacy

def load_movie_descriptions(filename):
    """
    Read movie descriptions from a file and return a dictionary mapping movie titles to their descriptions.
    """
    movie_descriptions = {}
    with open(filename, 'r') as file:
        for line in file:
            title, description = line.strip().split(':', 1)
            movie_descriptions[title.strip()] = description.strip()
    return movie_descriptions

def find_similar_movie(description, movie_descriptions):
    """
    Find the most similar movie based on word vector similarity of the given description.
    """
    nlp = spacy.load("en_core_web_md")
    max_similarity = -1
    most_similar_movie = None
    
    description_vector = nlp(description).vector
    for title, desc in movie_descriptions.items():
        sim_score = nlp(desc).similarity(description_vector)
        if sim_score > max_similarity:
            max_similarity = sim_score
            most_similar_movie = title
    
    return most_similar_movie

def main():
    movie_descriptions = load_movie_descriptions("movies.txt")
    description = "Will he save their world or destroy it? When the Hulk becomes too dangerous for the Earth, the Illuminati trick Hulk into a shuttle and launch him into space to a planet where the Hulk can live in peace. Unfortunately, Hulk land on the planet Sakaar where he is sold into slavery and trained as a gladiator."
    similar_movie = find_similar_movie(description, movie_descriptions)
    print("The movie you should watch next is:", similar_movie)

if __name__ == "__main__":
    main()
