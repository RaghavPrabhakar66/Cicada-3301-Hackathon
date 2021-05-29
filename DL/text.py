from sentence_transformers import SentenceTransformer

import numpy as np


class TextFilter:
    def __init__(self, threshold=0.45):
        self.model = SentenceTransformer('bert-base-nli-mean-tokens')
        self.threshold = threshold
    

    def generateFilter(self, textList, path):
        textEmbeds = self.model.encode(textList)
        meanEmbeds = np.mean(textEmbeds, axis=0)[np.newaxis, :]
        np.save(path, meanEmbeds)
        return meanEmbeds
