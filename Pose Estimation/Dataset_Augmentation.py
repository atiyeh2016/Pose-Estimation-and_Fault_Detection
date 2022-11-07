#%% Importing Librarires
from __future__ import print_function, division
from PoseDataset import PoseLandmarksDataset
from torchvision import transforms
import matplotlib.pyplot as plt
import numpy as np
import torch
from ToTensor import ToTensor
from Rotation import Rotation
from Scaling import Scaling
from Shearing import Shearing
from Translation import Translation
from Brighness import Brightness
from Contrast import Contrast

#%% Showing or not Showing
flag = 1

#%% Original Dataset
original = PoseLandmarksDataset('joints_train.csv',
                                        r'_images',
                                        transform=transforms.Compose([ToTensor()]))

#%% Rotation
rotated = PoseLandmarksDataset('joints_train.csv',
                                       r'_images',
                                       transform=transforms.Compose([Rotation(show = flag), ToTensor()]))

#%% Scaling
scaled = PoseLandmarksDataset('joints_train.csv',
                                       r'_images',
                                       transform=transforms.Compose([Scaling(show = flag), ToTensor()]))

#%% Shearing
sheared = PoseLandmarksDataset('joints_train.csv',
                                           r'_images',
                                           transform=transforms.Compose([Shearing(show = flag), ToTensor()]))

#%% Traslation
translated = PoseLandmarksDataset('joints_train.csv',
                                           r'_images',
                                           transform=transforms.Compose([Translation(show = flag), ToTensor()]))

#%% Brightness
brightness_changed = PoseLandmarksDataset('joints_train.csv',
                                                r'_images',
                                                transform=transforms.Compose([Brightness(show = flag), ToTensor()]))
test_image = brightness_changed[0] 

#%% Contrast
contrast_changed = PoseLandmarksDataset('joints_train.csv',
                                                r'_images',
                                                transform=transforms.Compose([Contrast(show = flag), ToTensor()]))
#%% Concating datasets
final_dataset = torch.utils.data.ConcatDataset((original, rotated, scaled,
                                                sheared, brightness_changed, contrast_changed))
def show_landmarks(image, landmarks=[]):
    image = np.array(image)
    image = image.transpose((1, 2, 0))
    plt.imshow(image)
    plt.scatter(landmarks[:, 0], landmarks[:, 1], s=10, marker='.', c='r')
    plt.pause(0.001)  # pause a bit so that plots are updated

test_image = final_dataset[0] # 8394 photos
fig = plt.figure()
#    sample = pose_dataset[5]
show_landmarks(**test_image)