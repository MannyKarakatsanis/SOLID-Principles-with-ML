"""
    SO>L<ID 
    L = liskov substitution method

    definition:
    "is S is a subtype of T, then objects of type T may be 
    replaced by objects of type S, without disrupting the program" 
"""


from abc import abstractmethod, ABC

class Extractor(ABC):

    @abstractmethod
    def extract(self, data):
        pass

class MelSpectrogramExtractor(Extractor):

    def __init__(self, num_mels):
        self.num_mels = num_mels

    def extract(self, data):
        print("Extracted mel spectrogram")

class MFCCExtractor(Extractor):
    def __init__(self, num_mfccs):
        self.num_mfccs = num_mfccs

    def extract(self, data):
        print("Extracted mfcc")



if __name__ == "__main__":
    data = [1, 2, 3]
    extractor = MFCCExtractor(13)
    extractor.extract(data)