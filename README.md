# Python YouTube Downloader

This Python project lets you download YouTube videos or audios to your local system using a provided link.

## Features

- Download a YouTube video in the highest available resolution.
- Download just the audio of a YouTube video.
- User friendly: simply enter a YouTube link and choose whether to download the video or audio.

## Usage

1. Run the python file in a terminal: `python main.py`
2. When prompted, enter the YouTube link for the video you want to download.
3. Choose whether you want to download the video or just the audio by typing either 'video' or 'audio' when prompted.

## Example

```bash
Please enter the YouTube link: https://www.youtube.com/watch?v=dQw4w9WgXcQ
Title: Rick Astley - Never Gonna Give You Up (Video)
Do you want to download the video or just the audio? Enter 'video' or 'audio': video
Your video has downloaded!
```

## Dependencies

This project uses the [pytube](https://pypi.org/project/pytube/) Python library to interact with YouTube videos. You can install it using pip:

```bash
pip install pytube
```

## Issues

If you encounter the error `get_transform_object: could not find match for var for={(.*?)};`, try updating pytube to the latest version:

```bash
pip install --upgrade pytube
```

## Disclaimer

Please note that YouTube's Terms of Service generally prohibit the downloading of videos, and doing so may violate those terms. Use this code responsibly and in compliance with all applicable laws and regulations.