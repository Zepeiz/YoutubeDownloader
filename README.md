# YoutubeDownloader
Simple python command line tool to batch download youtube videos in mp3/mp4 format using pytube.
Currently supports downloading:
* mp3.
* mp4 up to 720p with audio.
* mp4 up to 1080pp without audio.
* Downloading multiple mp3 at a time.

## Setup
1. Have python installed
2. pip install pytube, or if you are running python3, do: pip3 install pytube
3. Download the source code
4. Run Main.py

## Guide to downloading multiple videos/audios at a time:
1. Create a source.txt file in the src directory
2. Paste the youtube links one per line
3. Run Main.py and choose batch converter mode

## Disclaimers
This project is made using [Pytube](https://github.com/pytube/pytube), as of writing this on 11/jun/2023, the function
to extract the video description is no longer working apparently due to Youtube's API changes, so all video descriptions right now
will show as No description.

This project is made for personal use only, I do not take liability for misconduct with what users do with the files they download
using this tool.
