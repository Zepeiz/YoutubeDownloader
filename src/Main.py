from pytube import YouTube
from pytube_mp3 import *
from LinkParser import *

class Main:

    filePath = 'src/source.txt'
    videoURL = None


    def batchConverter(self):
        parser = LinkParser(self.filePath)
        links = parser.parse()
        print(links)
        print("The length of the list is: " + str(len(links)))

    def customConverter(self):
        # url input from user
        self.videoURL = str(input("Enter the URL of the video you want to download: \n>> "))
        yt = YouTube(self.videoURL)

        format = str(input("Do you want to download as mp3 or mp4?\n (audio/video)\n"))

        if format == "audio":
            download_mp3(yt)
        elif format == "video":
            download_mp4(yt)
        else: return "Unsupported operation"

    def run(self):
        self.batchConverter()



if __name__== "__main__":
    main = Main()
    main.run()


