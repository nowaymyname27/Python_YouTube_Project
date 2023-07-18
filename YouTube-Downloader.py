# import the YouTube module from the pytube library, which we'll use to interact with YouTube videos
from pytube import YouTube
# import the argv function from the sys library, which lets us take command line arguments
from sys import argv

# get the first command line argument (the YouTube link)
link = argv[1]

# create a YouTube object for the video
yt = YouTube(link)

# print the video's title and view count
print('Title: ', yt.title)
print('Views: ', yt.views)

# get the video stream with the highest resolution
yd = yt.streams.get_highest_resolution()

# download the video and save it to the specified path
yd.download("/Users/Galock/Desktop/CS_Summer/Python_YouTube_Project/Downloaded-Videos")
