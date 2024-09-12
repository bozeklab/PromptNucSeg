import numpy as np
import matplotlib.pyplot as plt
import os

test_path_raw = 'datasets/lucchi/test/raw/'
prompt_path = 'prompts/lucchi/'
to_save = 'prompts/visual/lucchi/'
os.makedirs(to_save, exist_ok=True)

for file in os.listdir(test_path_raw):
    print(test_path_raw + file)
    if file[-3:] != 'png':
        continue

    im = plt.imread(test_path_raw + file)
    implot = plt.imshow(im, cmap='gray')

    a = np.load(prompt_path + file[:-4] + '.npy')

    categories = a[:, 2]
    colormap = np.array(['red', 'blue', 'green', 'brown'])

    plt.scatter(a[:, 0], a[:, 1], s=50, c=colormap[categories.astype(int)])
    plt.savefig(to_save + file)
    plt.clf()

