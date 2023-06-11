import math
from pytube import YouTube

class mp4Converter:


    def download(self, yt):
        print("Enter the destination (leave blank for current directory)")
        destination = str(input(">> ")) or "downloads/mp4"

#TODO: currently 1080 is not possible due to progressive format, needs to combine 1080p video only file with sound.
        print("Enter the resolution you want (leave blank for highest):\n Eg: 1080p, 720p, 480p, 360p, 240p, 144p")
        res = str(input(">>")) or 'highest'

        #progressive category to get streams with both audio and video, but is limited to 720p or lower
        my_streams = yt.streams.filter(progressive=True)

        for streams in my_streams:
            # print itag, resolution and codec format of Mp4 streams
            print(f"Video itag : {streams.itag} Resolution : {streams.resolution} VCodec : {streams.codecs[0]}")

        itag = input("Enter itag Value : ")
        video = yt.streams.get_by_itag(itag)


        video.download(output_path=destination)
        
        self.outputMessage(yt, video)

       

    def outputMessage(self, yt, video):
        res = video.resolution
        duration = yt.length
        description = yt.description
        author = yt.author
        thumbnail = yt.thumbnail_url

        print(yt.title + " has been successfully downloaded.")
        print("resolution:" + res)
        print("thumbnail image: " + thumbnail)
        print("description: " + description)
        print("author: " + author)

        print("duration: " + str(duration))
        print("duration: " + str(math.floor(duration/60)) + ":" + str(duration%60))



