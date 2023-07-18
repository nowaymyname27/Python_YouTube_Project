# Import the YouTube module from the pytube library to interact with YouTube videos
from pytube import YouTube
# Import the argv function from the sys library to handle command line arguments
from sys import argv

# Get the first command line argument which should be the YouTube link
youtube_link = argv[1]

# Create a YouTube object for the video corresponding to the given link
youtube_video = YouTube(youtube_link)

# Print the video's title and view count
print('Title: ', youtube_video.title)
print('Views: ', youtube_video.views)

# Get the video stream with the highest resolution
highest_res_stream = youtube_video.streams.get_highest_resolution()

# Download the video and save it to the specified path
download_path = "/Users/Galock/Desktop/CS_Summer/Python_YouTube_Project/Downloaded-Videos"
highest_res_stream.download(download_path)
