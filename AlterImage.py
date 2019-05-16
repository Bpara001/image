import scipy.misc
from scipy.ndimage import gaussian_filter
import matplotlib.pyplot as plt
from scipy import misc
def imageShower(image):
    plt.figure()
    plt.imshow(image)
    plt.show()

def imageShowerGrey(image):
    plt.gray()
    plt.imshow(image)
    plt.show()

def main():
    ascent = scipy.misc.ascent()

    img2= scipy.misc.ascent()
    img3=gaussian_filter(img2,sigma=5)

    imageShower(img3)
    imageShowerGrey(img2)



if __name__ == "__main__":
    main()
