import torch
import torch.nn as nn
import torchvision.models as models
import torchvision.transforms as transforms
import numpy as np
import matplotlib.pyplot as plt
import cv2

class Model(Module):
    """
    CNN encoder using pretrained models
    """
    def __init__(self, backbone):
        super(Model, self).__init__()
        self.base_model = models.inception_v3(pretrained=True)
        print(self.base_model)
        self.base_model.fc = nn.Identity()

    # Foward pass
    def forward(self, input):
        x = self.base_model(input)

        return x
from PIL import Image
from tqdm import tqdm
import os

class Img2Vec:
    def __init__(self, size, device='auto'):
        '''
        Arguments:
            device : 'cpu', 'gpu', 'auto'
            size   : (int) Height = Width
        '''
        if device == 'cpu':
            self.device = 'cpu'
        elif device == 'gpu':
            self.device = 'gpu'
        else:
            self.device = 'gpu' if torch.cuda.is_available() else 'cpu'
        
        self.size = size

        self.resize = transforms.Resize((self.size, self.size))
        self.normalize = transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
        self.to_tensor = transforms.ToTensor()

        self.model = None
            
    def get_image(self, path):
        img = Image.open(path)
        img_processed = Variable(self.normalize(self.to_tensor(self.resize(img))).unsqueeze(0))

        return img_processed

    def cosine_similarity(self, vec1, vec2):
        cossimilarity = nn.CosineSimilarity(dim=0, eps=1e-6)

        return cossimilarity(vec1, vec2)

    def get_model(self, model_name):
        return Model(model_name)

    def get_vectors(self, img_processed):
        return self.model(img_processed)
    
    def run(self, path1, path2):
        img1 = self.get_image(path1)
        img2 = self.get_image(path2)

        self.model = self.get_model('vgg16')
        self.model.eval()
        
        final = []
        for i in tqdm(range(5)):
            vec1 = self.get_vectors(img1).squeeze(0)
            vec2 = self.get_vectors(img2).squeeze(0)
            print(vec1.shape)
            cos = self.cosine_similarity(vec1, vec2)
            final.append(cos.detach().numpy())
        print('\n',sum(final)/len(final))
  
  if __name__ == '__main__':
    img2vec = Img2Vec(224, 'auto')
    path1 = 'Path of Image 1'
    path2 = 'Path of Image 2'

    img2vec.run(path1, path2)
