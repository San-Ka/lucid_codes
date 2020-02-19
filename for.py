surveys = [123, 456, 789]

for survey in surveys:
    #do boring close survey stuff
    print('survey #' + str(survey) + ' closed')

for i in range(6):
    print(str(i))
for i in range(6,12):
    print(i)
#for/.keys()
movies = {"2001": "David", "Jurassic Park": "James bernard", "Rising Star": "Steve Thomas"}
for movie_name in movies.keys():
    print(movie_name) 
for director in movies.values():
    print(director)
for movie, director in movies.items():
    print(director + " directed " + movie )  
