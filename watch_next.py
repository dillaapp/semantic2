import spacy

# Load en_core_web_md
nlp = spacy.load('en_core_web_md')

# Declaring empty dictionary
movie_dic = {}

# Declaring empty list
movie_list = []


def read_file(filename):
    """
    This method will read file with movie names and description in it and give us dictionary {'movie_name':'movie description'}
    and list(list of movies)
    :param filename:  Text file name
    :return: adds dict value into movie_dic and add list values into movie_list
    """
    # open the movies.txt file
    file = open(filename, "r")

    # read the file line by line
    lines = file.readlines()

    # Looping through the lines and storing movie_name and movie_description in dic format
    for line in lines:
        line = line.strip()
        line = line.split(" :")
        movie_name = line[0].strip(",")
        Movie_description = line[1]

        # Adding values to line_dic
        movie_dic[movie_name] = Movie_description

        # Adding values to username_list
        movie_list.append(movie_name)

    # print(line_dic)
    # print(line_list)

    # close the file
    file.close()


# Your task is to create a function to return which movies a user would watch
# The function should take in the description as a parameter and return the
# title of the most similar movie.


def calc_similariy(filename, input_movie_disc_token):
    read_file(filename)

    # Declaring empty dictionary
    similarity_dic = {}

    # loop through the movie_dic and calculate similarity with input_movie_disc_token
    for movie_name, discription in movie_dic.items():
        similarity = nlp(movie_dic[movie_name]).similarity(input_movie_disc_token)
        # Adding values to similarity_dic
        similarity_dic[movie_name] = similarity

        # print(movie_name + " - ", similarity)
    # print(similarity_dic)

    # loop through the similarity_dic and get the movie with the highest similarity to the movie in question
    max_value = max(similarity_dic.values())
    for key, value in similarity_dic.items():
        if value == max_value:
            print("The movie with the highest similarity is '" + key + "' with a value of " + str(max_value))


# Input value: dictionay with movie name as a key and movie discription as value
movie_input = {
    'Planet Hulk': '''Will he save their world or destroy it? When the Hulk becomes too dangerous for the Earth, 
the Illuminati trick Hulk into a shuttle and launch him into space to a planet where the Hulk can live in peace. 
Unfortunately, Hulk land on the planet Sakaar where he is sold into slavery and trained as a gladiator '''
}

# create tokens for movie_description input
input_movie_disc_token = nlp(movie_input['Planet Hulk'])

# Run calc_similarity method
calc_similariy("movies.txt", input_movie_disc_token)
