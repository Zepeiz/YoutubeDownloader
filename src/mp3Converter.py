# importing packages
import math
from pytube import YouTube
import os
from pydub import AudioSegment

class mp3Converter:


    def download(self, yt):
#TODO: Add exception handling

        streams = yt.streams.filter(only_audio=True)
        file = yt.streams.get_by_itag(self.itagPicker(streams))
        # check for destination to save file
        destination = self.destinationPicker()

        # download the file
        out_file = file.download(output_path=destination)

        # rename the file
        self.extractMP3(yt, out_file)

        # result of success
        self.outputMessage(yt, file)

    def batchDownload(self, yt, destination):
#TODO: Add exception handling

        streams = yt.streams.filter(only_audio=True)
        #itag 140 for 128kbps mp3 format
        file = yt.streams.get_by_itag(140)
        # download the file
        out_file = file.download(output_path=destination)

        # rename the file
        self.extractMP3(yt, out_file)

        # result of success
        self.outputMessage(yt, file)


    def outputMessage(self, yt, file):
        duration = yt.length
        description = yt.description
        author = yt.author
        thumbnail = yt.thumbnail_url


        if(description == None):
            description = "No description"


        print(yt.title + " "+file.abr + " has been successfully downloaded.")
        print("thumbnail image: " + thumbnail)
        print("description: " + description)
        print("author: " + author)
        print("duration: " + str(math.floor(duration/60)) + ":" + str(duration%60) + "\n")

    def itagPicker(self, streams):
        for stream in streams:
            print(f"Itag : {stream.itag}, Quality : {stream.abr}, VCodec : {stream.codecs[0]}")

        # itag number 140 for mp3 128kbps
        itag = input("Enter itag Value (Leave blank for 128kbps) : ") or 140
        return itag

    def destinationPicker(self):
        print("Enter the destination (leave blank for current directory)")
        #relative path
        destination = str(input(">> ")) or "downloads/mp3"
        return destination

    #out_file is downloaded as VCodec : mp4a.40.2, then the mp3 needs to be extracted using pydub.
    def extractMP3(self, yt, out_file):
        file_path = os.path.abspath(out_file)
        audio = AudioSegment.from_file(file_path, format='mp4')

        #Changing the file name
        directory_path = os.path.dirname(out_file)
        file_name = os.path.basename(out_file)
        name, extension = os.path.splitext(file_name)
        new_file_name = yt.author + ' - ' + name + '.mp3'
        new_file = os.path.join(directory_path, new_file_name)

        #Exporting the mp3 into the new file path
        audio.export(new_file, format='mp3')

        #Deletes the now useless mp4 source file
        os.remove(file_path)

    def defaultFileName(self, out_file):
        name, extension = os.path.splitext(out_file)
        new_file = name + '.mp3'
        os.rename(out_file, new_file)


