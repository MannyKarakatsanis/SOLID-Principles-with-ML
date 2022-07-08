""""
    S>O<LID 
    O = open/closed principle

    definition: 
    "Software entities (classes, modules, methods etc)
    should be open for extension, but closed for modification."

    if you want to add functionality, do not modify, but instead add seperately.
"""

from abc import abstractmethod, ABC

class Extractor(ABC):

    @abstractmethod
    def extract(self, data):
        pass

class SpectrogramExtractor(Extractor):

    def extract(self, data):
        print("Extracted spectrogram")

class MelSpectrogramExtractor(Extractor):

    def extract(self, data):
        print("Extracted mel spectrogram")

class MFCCExtractor(Extractor):
    def extract(self, data):
        print("Extracted mfcc")

class OCP_Pipeline:

    def __init__(self, extractor):
        self.extractor = extractor

    def run(self, data):
        print("Running DL pipeline")
        features = self._extract(data)
    
    def _extract(self, data):
        self.extractor.extract(data)


if __name__ == "__main__":
    data = [1, 2, 3]
    extractor = SpectrogramExtractor()
    ocp_pipeline = OCP_Pipeline(extractor)
    ocp_pipeline.run(data)