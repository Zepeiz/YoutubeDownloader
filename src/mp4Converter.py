import math
from pytube import YouTube
import subprocess
import os
import re


class mp4Converter:
    invalid_symbols = r'[\\/:<>"|?*]'

    def download(self, yt):
        print("Enter the destination (leave blank for current directory)")
        destination = str(input(">> ")) or "downloads/mp4"

        # TODO: currently 1080 is not possible due to progressive format, needs to combine 1080p video only file with sound.
        print(
            "Enter the resolution you want (leave blank for highest):\n Eg: 1080p, 720p, 480p, 360p, 240p, 144p"
        )
        res = str(input(">>")) or "highest"

        # progressive category to get streams with both audio and video, but is limited to 720p or lower
        # my_streams = yt.streams.filter(progressive=True)

        # for streams in my_streams:
        #     # print itag, resolution and codec format of Mp4 streams
        #     print(
        #         f"Video itag : {streams.itag} Resolution : {streams.resolution} VCodec : {streams.codecs[0]}"
        #     )

        # itag = input("Enter itag Value : ")
        # video = yt.streams.get_by_itag(itag)

        # video.download(output_path=destination)
        video = None
        if res == "highest" or int(res.replace("p", "")) > 720:
            video = yt.streams.filter(adaptive=True)

            for stream in video:
                # print itag, resolution and codec format of Mp4 streams
                print(
                    f"Video itag : {stream.itag} Resolution : {stream.resolution} VCodec : {stream.codecs[0]}"
                )
            itag = input("Enter itag Value : ")
            video = yt.streams.get_by_itag(itag)

            audio = yt.streams.get_by_itag(140)  # 140 = 128kbps audio
            video.download(output_path=destination, filename="video.mp4")
            audio.download(output_path=destination, filename="audio.mp4")
            subprocess.run(
                [
                    "ffmpeg",
                    "-i",
                    os.path.join(destination, "video.mp4"),
                    "-i",
                    os.path.join(destination, "audio.mp4"),
                    os.path.join(destination, self.filter_file_name(yt.title) + ".mp4"),
                ]
            )
            os.remove(os.path.join(destination, "video.mp4"))
            os.remove(os.path.join(destination, "audio.mp4"))
        else:
            my_streams = yt.streams.filter(progressive=True)

            for streams in my_streams:
                # print itag, resolution and codec format of Mp4 streams
                print(
                    f"Video itag : {streams.itag} Resolution : {streams.resolution} VCodec : {streams.codecs[0]}"
                )

            itag = input("Enter itag Value : ")
            video = yt.streams.get_by_itag(itag)
            video.download(output_path=destination)

        self.outputMessage(yt, video)

    def outputMessage(self, yt, video):
        res = yt.resolution if yt.resolution else "Resolution unavailable"
        duration = yt.length if yt.length else 0
        description = yt.description if yt.description else "No description"
        author = yt.author if yt.author else "Author unavailable"
        thumbnail = yt.thumbnail_url if yt.thumbnail else "Thumbnail unavailable"

        print(yt.title + " has been successfully downloaded.")
        print("resolution:" + res)
        print("thumbnail image: " + thumbnail)
        print("description: " + description)
        print("author: " + author)

        print("duration: " + str(duration))
        print("duration: " + str(math.floor(duration / 60)) + ":" + str(duration % 60))

    def rename(self, out_file):
        # First separate directory path with file name
        # Then separate file name with its extension
        # Filter the file name, then join back the extension
        # Then join back the new file name with the same directory as before
        # Then replace the old file with the new file

        directory_path = os.path.dirname(out_file)
        base_name = os.path.basename(out_file)

        name, extension = os.path.splitext(base_name)
        new_name = self.filter_file_name(name)
        new_basename = new_name + extension
        new_file = os.path.join(directory_path, new_basename)
        os.rename(out_file, new_file)
        return new_file

    def filter_file_name(self, file_name):

        # Remove the invalid symbols from the file name
        filtered_name = re.sub(self.invalid_symbols, "", file_name)

        return filtered_name

    def contains_invalid_symbols(self, file_name):

        # Check if the file name contains any invalid symbols
        if re.search(self.invalid_symbols, file_name):
            return True
        else:
            return False
