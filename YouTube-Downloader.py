# Import the YouTube module from the pytube library to interact with YouTube videos
from pytube import YouTube

# Get the YouTube link from the user
youtube_link = input("Please enter the YouTube link: ")

try:
    # Create a YouTube object for the video corresponding to the given link
    youtube_video = YouTube(youtube_link)

    # Print the video's title
    print('Title: ', youtube_video.title)

    # Get the video stream with the highest resolution
    highest_res_stream = youtube_video.streams.get_highest_resolution()

    # Download the video and save it to the specified path
    download_path = "/Users/Galock/Desktop/CS_Summer/Downloaded-Videos"
    highest_res_stream.download(download_path)

    # Print a success message
    print("Your video has downloaded!")

except Exception as e:
    # If an error occurred, print an error message
    print("The video failed to download... :(")
    print("Error details: ", str(e))
