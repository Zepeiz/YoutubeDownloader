# importing packages
from pytube import YouTube
import os
from pytube_mp4 import *

def download_mp3(yt):

    # extract only audio
    streams = yt.streams.filter(only_audio=True)

    for stream in streams:
        print(f"Itag : {stream.itag}, Quality : {stream.abr}, VCodec : {stream.codecs[0]}")

    itag = input("Enter itag Value : ")
    file = yt.streams.get_by_itag(itag)

    # check for destination to save file
    print("Enter the destination (leave blank for current directory)")
    #relative path
    destination = str(input(">> ")) or "downloads/mp3"

    # download the file
    out_file = file.download(output_path=destination)

    # save the file

    base, ext = os.path.splitext(out_file)
    new_file = base + '.mp3'
    os.rename(out_file, new_file)

    # result of success
    duration = yt.length
    description = yt.description
    author = yt.author
    thumbnail = yt.thumbnail_url


    if(description == None):
        description = "No description"


    print(yt.title + " "+file.abr + " has been successfully downloaded.")
    print("thumbnail image: " + thumbnail)
    print("description: " + yt.description)
    print("author: " + author)
    print("duration: " + str(duration))
    print("duration: " + str(math.floor(duration/60)) + ":" + str(duration%60))



