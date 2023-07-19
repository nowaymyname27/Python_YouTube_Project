import subprocess
import sys
from tkinter import filedialog
from tkinter import Tk

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

    try:
        # Create a Tk window and immediately withdraw it to avoid an extra, empty window
        root = Tk()
        root.withdraw()

        # Open a file chooser dialog to select the download path and get the chosen path
        download_path = filedialog.askdirectory()

    except Exception as e:
        print("An error occurred while trying to select a download path.")
        print("Error details: ", str(e))
        exit()
        
    # Download the chosen stream and save it to the specified path
    chosen_stream.download(download_path)

    # Print a success message
    print("Your {} has downloaded!".format(download_choice))

except Exception as e:
    # If an error occurred, print an error message
    print("The {} failed to download... :(".format(download_choice))
    print("Error details: ", str(e))
