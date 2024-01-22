#Spotify Data Analyzer
#Author: Hashim
#16 january 2024

#version 0.1
#  -From the data set get all the songs 
#   performed by drake

import csv
#Open up the file
with open("./spotify (1).csv") as f:
    #----- Look for all songs performed by Drake
    #      Use linear search
    #Create a csv reader object
    csv_reader = csv.DictReader(f)

    #Create a list to store all Drake's songs
    drake_songs = []

    #Create a counter for the current line number

    #For every song in the .csv file 
    for line in csv_reader:
        if "Drake".lower() in line["artist"].lower():
            #Add it to the song list
            drake_songs.append(
                (line["artist"], line["song_title"], line["danceability"])
            )
for song in drake_songs:
    if float(song[-1]) >= 0.6:
        print(song)

# Print out all songs that have
# a danceability of >= 0.6