# Python YouTube Downloader

This is a simple script to download videos or audio from YouTube.

## Features

1. Downloads video or audio-only from a YouTube link provided by the user.
2. Automatically updates the required library `pytube`.
3. User can choose the download path via a GUI-based folder picker.

## Usage

Run the `YouTube-Downloader.py` script. You will be prompted to:

1. Enter a YouTube link.
2. Choose whether to download the video or just the audio.

Next, a dialog box will open, allowing you to choose a download location. After you've chosen the download path, the selected YouTube video or audio will begin to download.

Please note that you need to have `tkinter` and `pytube` installed for the script to work properly. These should be automatically updated and handled by the script.

## Possible Errors

If an error occurs, an error message will be displayed, providing the details of what went wrong. If the error occurs during the download process, it will notify you that the download failed. If the error occurs while selecting the download path, it will inform you that an error occurred during the selection process.

## Creating Executable

For ease of use, consider packaging this script into an executable file using tools like PyInstaller. This way, users won't need to have Python or the required packages installed on their system.

Refer to the Python packaging documentation or the PyInstaller documentation for instructions on how to do this. Be sure to thoroughly test your packaged application to ensure everything works as expected.