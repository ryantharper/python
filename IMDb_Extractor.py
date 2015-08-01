import urllib2 as u
import json, sys

yes = ["yes", "ye", "y", "yh", "ya", "yah", "yeah"] # different types of yes strings
no = ["no", "na", "n", "nh", "nah", "neh"]
# desired keys for searches w/o season and episode
desiredNorm = ['Title', 'Year', 'Runtime', 'Genre', 'Actors', 'Plot', 'imdbRating']
# desired keys for searches WITH season and episode
desiredSE = ['Title', 'Season', 'Episode', 'Actors', 'Plot', 'imdbRating']

def listJSONLoads(norm, jsonLd): # boolean, json.loads file
    if norm == True: # if user DID NOT enter season & episode values
        for element in desiredNorm:
            # e.g. this would print ->   Title: Breaking Bad
            print element + ": " + jsonLd[str(element)] + "\n" 
    else:
        for element in desiredSE: # if user entered season and ep values
            print element + ": " + jsonLd[str(element)] + "\n"

def openURL(url, normOrNot):
    resp = u.urlopen(url)
    resp = json.loads(str(resp.read()))
    listJSONLoads(normOrNot, resp)

def seasonAndEpisode(search, lp):
    seasn = raw_input("Season: ")
    ep = raw_input("Episode: ")

    search = search.replace(" ", "+")
    if lp == True: # if user wants long plot
        url = "http://www.omdbapi.com/?t=%s&Season=%s&Episode=%s&plot=full&r=json" % (search, seasn, ep)
    else: # if user wants short plot
        url = "http://www.omdbapi.com/?t=%s&Season=%s&Episode=%s&r=json" % (search, seasn, ep)
        
    openURL(url, False)

def normalSearch(search, lp):
    search = search.replace(" ", "+")

    if lp == True:
        url = "http://www.omdbapi.com/?t=%s&plot=full&r=json" % search 
        
    else:
        url = "http://www.omdbapi.com/?t=%s&r=json" % search 

    openURL(url, True)
def Main():
    search = raw_input("What film or TV show would you like to search for? ").title()
    seasonQ = raw_input("Would you like to search for a specic episode from a season? Enter yes or no: ")
    longPlot = raw_input("Would you like the long plot? Enter yes or no: ")

    if seasonQ in yes and longPlot in yes:
        seasonAndEpisode(search, True)
    elif seasonQ in yes and longPlot in no:
        seasonAndEpisode(search, False)
    elif seasonQ in no and longPlot in yes:
        normalSearch(search, True)
    elif seasonQ in no and longPlot in no:
        normalSearch(search, False)
    else:
        print "I did not understand. Exiting."
        sys.exit()
if __name__ == '__main__':
    Main()
    
