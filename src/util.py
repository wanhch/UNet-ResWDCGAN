import numpy as np
import matplotlib.image as mpimg
import cv2
import pandas as pd
import os
# from PIL import Image


def sample_noise(size, mu=0., sigma=1.):
    return np.random.normal(mu, sigma, size=size)

'''
def getData(path, size, value="mel"):
	DF = pd.read_pickle(path)
	assert(len(DF["image"]) == len(DF["id"]))

	X = []
	for i in range(len(DF["image"])):

		if DF["id"][i] == value:
			tmp = cv2.resize(DF["image"][i], (int(size), int(size)), interpolation=cv2.INTER_CUBIC)
			result = (tmp - 127.5) / 127.5
			X.append(result)

	return np.array(X, dtype=np.float32)
'''

def getData(path, size):
    img_list = os.listdir(path)
    X = []
    count = 0
    for img_str in img_list:
        # count += 1
        # if (count == 100):
        #     break;
        # image = Image.open(path + "\\" + img_str)
        # image = image.convert(mode='RGB')
        # result = np.asarray(image)
        image = cv2.imread(path + "/" + img_str)
        image = cv2.resize(image, (int(size), int(size)), interpolation=cv2.INTER_CUBIC)
        result = (image -127.5) / 127.5
        X.append(result)
    return np.array(X, dtype=np.float32)



def saveImages(filename, images):    
    for i in range(len(images)):
        mpimg.imsave(filename + "-" + str(i) + ".png",  ( (images[i] * 127.5) + 127.5 ).astype(np.uint8))