from PIL import Image
from tqdm import tqdm
import os
import torch
import torch.nn as nn
import torchvision.models as models
import torchvision.transforms as transforms
import numpy as np
import matplotlib.pyplot as plt
import cv2
from torch.autograd import Variable
from torch.nn import Module

class Model(Module):
    def __init__(self, backbone):
        super(Model, self).__init__()
        self.base_model = models.inception_v3(pretrained=True)
        self.base_model.fc = nn.Identity()

    def forward(self, input): return self.base_model(input)

class ImgFilter:
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
            
    def process_image(self, img):
        return Variable(self.normalize(self.to_tensor(self.resize(img))).unsqueeze(0))
    
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

    def generate_np(self, label, files):
        self.model = self.get_model('vgg16')
        self.model.eval()

        final = []
        for i in range(3):
            path = '/content/seg_train/seg_train/' + label + '/' + files[i]
            print(path)
            img = self.get_image(path)
            vec = self.get_vectors(img).squeeze(0)
            final.append(vec.detach().numpy())
        mean = np.mean(final, axis=0)
        np.save(f'{label}', mean)
    
    def run(self, embed_file_path, img):
        self.model = self.get_model('vgg16')
        self.model.eval()
        stored_embed = None

        img = self.process_image(img)

        if os.path.isfile(embed_file_path):
            stored_embed = np.load(embed_file_path)
            vec = self.get_vectors(img).squeeze(0)
            cos = self.cosine_similarity(torch.from_numpy(stored_embed), vec)
            mean = np.mean([stored_embed, vec.detach().numpy()], axis=0)
            return (True, mean) if cos >= 0.50 else (False, mean)
        else:
            print ("File not exist")
            exit()

if __name__ == '__main__':
    img_filter = ImgFilter(224, 'auto')
    img = Image.open('/content/seg_train/seg_train/forest/18363.jpg')
    res, mean = img_filter.run('/content/forest.npy', img)
