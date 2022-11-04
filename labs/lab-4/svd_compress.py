import matplotlib.pyplot as plt    # need for plotting an image
import matplotlib.image as mpimg   # need for image loading and saving
import numpy as np                 # need for manipulating arrays
from numpy import linalg as la     # need for finding SVD

img = mpimg.imread('octopus.jpg')        # you need to download the image from Canvas/Files/Labs
plt.imshow(img)
plt.show()
X, Y, Z = img.shape                # get the image array dimensions


# apply SVD to all pixels at once
img_transposed = np.transpose(img, (2, 0, 1))
U, s, Vt = la.svd(img_transposed)

# create diagonal array
Sigma = np.zeros((Z, X, Y))
for j in range(3):
    np.fill_diagonal(Sigma[j, :, :], s[j, :])

# truncate array 
k = 50    
img_approx = U @ Sigma[..., :k] @ Vt[..., :k, :] 
img_approx = np.transpose(img_approx, (1, 2, 0))  
img_approx = img_approx - img_approx.min()   
img_approx = img_approx / img_approx.max()

# show compressed image and save file
plt.imshow(img_approx)  
plt.show()
plt.imsave("octopus_new.jpg", img_approx)