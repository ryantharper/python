import urllib2 as u
import json, sys, os

path = '/home/ryan/python/movies_folder'

movieList = os.listdir(path)

dbHeaders = ['Title', 'Year', 'Genre', 'Plot', 'imdbRating']

f = open("/home/ryan/movies.txt", "w")   

def searchMovie(film):
    film = film.replace(" ", "+")
    url = "http://www.omdbapi.com/?t=%s&r=json" % film
    resp = u.urlopen(url)
    resp = json.loads(str(resp.read()))
    
    for e in dbHeaders:
        f.write(resp[e] + "\t")
    

for movie in movieList:
    searchMovie(movie)
    f.write("\n")
