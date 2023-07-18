```markdown
# Python YouTube Downloader

This is a simple Python script that uses the `pytube` library to download a YouTube video. Given a YouTube link, it will download the highest resolution stream available.

## Dependencies

This script requires Python 3 and the `pytube` library. You can install `pytube` with pip:

```bash
pip install pytube
```

## Usage

This script takes a YouTube link as a command-line argument and downloads the video to a specific path on your system.

To use the script, you can run it from the command line as follows:

```bash
python your_script_name.py https://www.youtube.com/watch?v=dQw4w9WgXcQ
```

Replace `https://www.youtube.com/watch?v=dQw4w9WgXcQ` with the link of the YouTube video you want to download. 

The downloaded video will be stored in the following path: `/Users/Galock/Desktop/CS_Summer/Python_YouTube_Project/Downloaded-Videos`.

## What the Script Does

After receiving the YouTube link as an argument, the script uses the `pytube` library to create a `YouTube` object.

It then prints out the title of the video and the number of views it has.

Finally, it downloads the highest resolution stream available for that video.

Please note, the download path is hard-coded, you may need to adjust it based on your system configuration.
```
Replace `your_script_name.py` with the name of your script file. Also, adjust any other details according to your needs.
