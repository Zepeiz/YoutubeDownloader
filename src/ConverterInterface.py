import abc

class ConverterInterface(metaclass = abc.ABCMeta):
    @classmethod
    def __subclasshook__(cls, __subclass: type) -> bool:
        return (hasattr(__subclass, 'download') and
                callable(__subclass.download) # type: ignore
        )
    # __subclasshook will automatically register a class as a subclass of current class if it matches the conditions specified:
    # It must have an attribute called 'download' and it must also be callable, meaning there has to be a method called 'download'.
    
    # Abstract methods must not have body and be implemented in a concrete subclass
    # Concrete methods can be used directly or overridden

    @abc.abstractmethod 
    def download(self, yt):
        #Downloads from a single link at a time
        streams = yt.streams.filter
        pass

    @abc.abstractmethod 
    def batchDownload(self):
        #Downloads from multiple links at a time
        pass

    @abc.abstractmethod
    def outputMessage(self):
        #Downloads
        pass
    
    @abc.abstractmethod
    def itagPicker(self, streams) -> int:
        for stream in streams:
            print(f"Itag : {stream.itag}, Quality : {stream.abr}, Resolution : {streams.resolution}, VCodec : {stream.codecs[0]}")
        # itag number 140 for mp3 128kbps, 37 for 1080p mp4
        itag = int(input("Enter itag Value"))
        return itag
    
    def destinationPicker(self) -> str:
        print("Enter the destination (leave blank for current directory)")
        #relative path
        destination = str(input(">> ")) or "downloads"
        return destination

class TestClass(object):
    def download(self):
        pass

print(issubclass(TestClass, ConverterInterface))
