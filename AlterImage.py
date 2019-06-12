import scipy.misc
from scipy.ndimage import gaussian_filter
import matplotlib.pyplot as plt
import os,glob,cv2
from os import path
from scipy import misc
from scipy.ndimage import gaussian_filter
import matplotlib.image as mpimg
from PIL import Image
from IPython.display import set_matplotlib_formats
def rgb2gray(rgb):
    return np.dot(rgb[...,:3], [0.2989, 0.5870, 0.1140])

import numpy as np
def imageShower(image,i):
    fig=plt.figure()
    plt.axis('off')
    plt.imshow(image)
    temp = str(i)
    file_gauss = temp + 'gauss.jpg'
    plt.savefig(path.join('Gauss2/', file_gauss),bbox_inches='tight',pad_inches=0)

def main():

    path = r'C:\Users\Jesse\PycharmProjects\image\Pictures\Casia2\Au'
    i = 0
    for filename in glob.glob(os.path.join(path,'*.jpg')):
        with open(filename, 'r') as f:
            #print(filename)
            image = (mpimg.imread(filename))
            print(image.shape)
            alter = gaussian_filter(image, sigma=2)
            imageShower(alter,i)
            i =i+1

#gaussian_filter(image,sigma=5)


if __name__ == "__main__":
    main()
