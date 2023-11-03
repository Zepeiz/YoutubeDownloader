from pytube import YouTube
from mp3Converter import *
from mp4Converter import *
from LinkParser import *

class Main:

    filePath = 'src/source.txt'
    videoURL = None
    mp3_converter = mp3Converter()
    #mp4_converter = mp4Converter()
    exit = False


    #Only for mp3
    def batchConverter(self):
        parser = LinkParser(self.filePath)
        #array of links
        links = parser.parse()
        print(links)
        length = len(links)
        print("The length of the list is: " + str(length))

        destination = self.mp3_converter.destinationPicker()

        for i in range(length):
            try:
                yt = YouTube(links[i])
                yt.check_availability()
                print("Current progress: " + str(i+1) + "/" + str(length))
                print("Downloading: " + yt.title + "\n")
                self.mp3_converter.batchDownload(yt, destination)
            except Exception:
                print("Video unavailable.")
                continue
        print("Batch download complete!\n")


    def customConverter(self):
        # url input from user
        videoURL = str(input("Enter the URL of the video you want to download: \n>> "))
        yt = YouTube(videoURL)

        format = str(input("Do you want to download as mp3 or mp4?\n (audio/video)\n"))

        if format == "audio":
            self.mp3_converter.download(yt)
        #elif format == "video":
            #self.mp4_converter.download(yt)
        else: print("Unsupported operation")




    def run(self):
        while not self.exit:

            option = input("Do you want to convert from source.txt or a single link?'\n(source/single)").lower()
            if(option == "source"):
                self.batchConverter()
            elif option == "single":
                self.customConverter()
            else:
                print("Invalid argument")

            self.chooseToExit()
        print("Thanks for using the tool! <3")

    def chooseToExit(self):
        option = input("Continue?\n(Y/N)").lower()
        if option == "n":
            self.exit = True
        else:
            pass

if __name__== "__main__":
    main = Main()
    main.run()


