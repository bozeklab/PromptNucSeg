import numpy as np
import matplotlib.pyplot as plt


image_names = ['2_' + str(i) for i in range(30)] + ['3_' + str(i) for i in range(30)]
for image_name in image_names:
    im = plt.imread('datasets/pannuke/Images/' + image_name + '.png')
    implot = plt.imshow(im)

    a = np.load('prompts/pannuke123/' + image_name + '.npy')

    #print(a)
    print(a.shape)

    categories = a[:, 2]
    colormap = np.array(['green', 'blue', 'red', 'brown'])

    plt.scatter(a[:, 0], a[:, 1], s=50, c=colormap[categories.astype(int)])
    plt.savefig('prompts/visual/new_repo/' + image_name + '.png')
    plt.clf()

