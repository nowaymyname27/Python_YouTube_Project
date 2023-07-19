import subprocess
import sys

def update_pytube():
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', '--upgrade', 'pytube'])

update_pytube()

# Import the YouTube module from the pytube library to interact with YouTube videos
from pytube import YouTube

# Get the YouTube link from the user
youtube_link = input("Please enter the YouTube link: ")

try:
    # Create a YouTube object for the video corresponding to the given link
    youtube_video = YouTube(youtube_link)

    # Print the video's title
    print('Title: ', youtube_video.title)

    # Ask the user if they want to download the video or just the audio
    download_choice = input("Do you want to download the video or just the audio? Enter 'video' or 'audio': ")

    # Based on the user's choice, get the appropriate stream
    if download_choice.lower() == 'video':
        chosen_stream = youtube_video.streams.filter(progressive=True).get_highest_resolution()
    elif download_choice.lower() == 'audio':
        chosen_stream = youtube_video.streams.filter(only_audio=True).first()
    else:
        print("Invalid choice, please enter either 'video' or 'audio'.")
        exit()

    # Download the chosen stream and save it to the specified path
    download_path = "/Users/Galock/Desktop/CS_Summer/Downloaded-Videos"
    chosen_stream.download(download_path)

    # Print a success message
    print("Your {} has downloaded!".format(download_choice))

except Exception as e:
    # If an error occurred, print an error message
    print("The {} failed to download... :(".format(download_choice))
    print("Error details: ", str(e))
