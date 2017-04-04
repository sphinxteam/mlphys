""" datasets.py

    A script to load in the datasets we will be using for TP04.
"""
import sys
import os
from skimage.io import imread
from skimage.transform import resize
import numpy as np

def load_lfw_dataset(data_home='mldata', min_num_faces=1, random_state=None, scale=0.5):
    """ load_lfw_dataset(data_home='mldata', num_num_faces=1)

        Load the dataset of LFW face images which have been aligned and 
        centered on the target face image.
    """
    dataset_dir = '%s/lfw-deepfunneled' % data_home
    images_to_process = []
    name_labels = []
    unique_names = []
    
    #--- Get list of name directories ---#
    names = os.listdir(dataset_dir)

    #--- Filter on number of images ---#
    label = -1
    for name in names:
        if name[0] != '.':
            name_dir = '%s/%s' % (dataset_dir, name)
            images_at_name = os.listdir(name_dir)

            ## Filter on number of images
            if len(images_at_name) >= min_num_faces:    
                unique_names.append(name)        
                label += 1    
                for imfile in images_at_name:
                    images_to_process.append('%s/%s' % (name_dir, imfile))
                    name_labels.append(label)    


    #--- Process images ---#
    name_labels = np.asarray(name_labels)
    n_images = len(images_to_process)
    new_dim  = (int(250*scale), int(250*scale))
    image_data = np.empty((n_images, new_dim[0], new_dim[1], 3), dtype=float) 

    for (idx, imfile) in enumerate(images_to_process):                   
        img = imread(imfile)

        ## Apply downsizing 
        if scale != 1.0:
            img = resize(img, new_dim, mode='reflect')

        ## Insert into dataset
        image_data[idx, :, :, :] = img

    #--- Shuffle Dataset ---#
    if random_state != None:
        np.random.seed(random_state)    

    perm_idx = np.random.permutation(n_images)
    image_data = image_data[perm_idx, :, :, :]
    name_labels = name_labels[perm_idx]

    return image_data, name_labels, unique_names
                    


def catdog_train_generator(data_home='./mldata'):
    """
        Gets a random selection of cats and dogs to fill the specified
        batch size.
    """
    n_cats = 12500
    n_dogs = 12500
    cat_prefix = '%s/%s' % (data_home, 'kaggle-catdog/train/cat.')
    dog_prefix = '%s/%s' % (data_home, 'kaggle-catdog/train/dog.')

    while 1:
        is_cat = np.random.randint(0,2)


# def get_random_catdog(batch_size=32):
#     """
#         Gets a random selection of cats and dogs to fill the specified
#         batch size.
#     """
#     cat_idx = np.random.randint(0, 2, size=batch_size)
#     # num_cats = np.random.randint(0,batch_size)

#     # Now, we will loop over the batch size and get these values
#     for i in range(batch_size):