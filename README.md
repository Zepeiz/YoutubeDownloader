# YoutubeDownloader
Simple python command line tool to batch download youtube videos in mp3/mp4 format using pytube.
Currently supports downloading:
* mp3 up to 128kbps
* mp4 up to 1080p with audio
* Downloading multiple mp3 at a time

## Setup
1. Have python installed
2. Install dependencies: `pip install -r requirements.txt`, or python3 if you are on Mac.
3. Install ffmpeg
	1. (Mac) `brew install ffmpeg`
	2. (Windows) https://ffmpeg.org/download.html. Then add the FFmpeg bin folder to your system's PATH variable:
		* Open the Start menu and search for "Environment Variables" or "Edit the system environment variables."
		* Click on the "Edit the system environment variables" option.
		* In the System Properties window, click on the "Environment Variables" button.
		* In the "System variables" section, find the "Path" variable and click on "Edit."
		* Click on "New" and add the full path to the bin folder of the extracted FFmpeg archive (e.g., C:\path\to\ffmpeg\bin).
		* Click "OK" to save the changes.
	3. (Linux) `sudo apt-get install ffmpeg`
5. Download the latest release zip file
6. Run `Main.py`, for downloading multiple at a time, look below.


## Guide to downloading multiple audio files at a time:
1. Create a `source.txt` file in the src directory
2. Paste the youtube links one per line
3. Run Main.py and choose source(multi) mode

## Disclaimers
This project is using [Pytube](https://github.com/pytube/pytube) to get files and metadata from Youtube, as of writing this on 11/jun/2023, the function
to extract the video description is no longer working apparently due to Youtube's API changes, so all video descriptions right now
will show as No description.

This project is made for personal use only, I do not take liability for misconduct with what users do with the files they download
using this tool.
