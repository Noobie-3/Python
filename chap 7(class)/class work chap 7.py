#Wizard Inventory 
#date 02/07/22

import pickle #Pickle Rick HAHAH

movies = [
    ["Monty Python", 1975],
    ["Cat on a Hot Tin Roof", 1958],
    ["On the Waterfront", 1964]
]

with open("movies.bin", "wb") as file:
    pickle.dump(movies,file)

with open("movies.bin", "rb") as file:
    movie_list = pickle.load(file)
    print(movie_list)


